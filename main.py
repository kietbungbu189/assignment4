from src.config import RAW_CSV
from src.extract import read_fact_csv
from src.transform import build_dim_supplier
from src.transform import build_dim_logistics
from src.transform import build_dim_product
from src.transform import attach_keys
from src.config import DB
from src.load import create_db
from src.validate import check_relationship
from src.validate import validate_warehouse
from src.analytics import check_low_stock
from src.analytics import priority_stock
from src.analytics import classify_stock
from src.analytics import total_revenue
from src.analytics import broadcast
from src.analytics import shipping_costs
from src.analytics import boxes_required
from src.log import log_analysis
from src.analytics import below_20_stock
from src.transform import options
from src.analytics import restock
from src.optimize import optimize
from src.config import MATERIAL_AUGUST, MATERIAL_OCTOBER
from src.extract import extract_materials
from src.analytics import check_material_balance
from src.config import MATERIAL_OFFERS

#Which materials are likely to run short, which vendor can cover the gap,...
# and how much cash and extra stock would that order create?

def main():
    print(f"Printing the first 5 rows of {RAW_CSV}")

    raw = read_fact_csv(RAW_CSV)
    suppliers = build_dim_supplier(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"Supplier-location combinations: {len(suppliers)}")
    print(suppliers.head())

    logistics = build_dim_logistics(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"Shipping carriers-Transportation modes-Routes combinations: {len(logistics)}")
    print(logistics.head())

    products = build_dim_product(raw)
    print(f"Raw rows: {len(raw)}")
    print(f"SKU records: {len(products)}")
    print(products.head())

    merge1 = attach_keys(raw, suppliers, ['Supplier name', 'Location'])
    merge2 = attach_keys(merge1, logistics, ['Shipping carriers', 'Transportation modes', 'Routes'])
    merge2 = merge2.drop(columns=['Supplier name', 'Location', 'Shipping carriers', 'Transportation modes', 'Routes', 'Product type', 'Price'])

    unified_monthly_main = extract_materials(MATERIAL_AUGUST, MATERIAL_OCTOBER)
    print(unified_monthly_main.head())

    matched_balance_main = check_material_balance(unified_monthly_main)

    create_db(products, logistics, suppliers, merge2)
    
    validate_warehouse(DB)

    low_stock = check_low_stock(merge2, 'Stock levels')
    print(low_stock.head())

    priority = priority_stock(merge2, 'Stock levels', 'Number of products sold')
    print(priority.head())

    classify = merge2['Stock levels'].apply(classify_stock)
    print(classify.head())

    total = total_revenue(merge2, 'Revenue generated')
    print(total)

    profit = broadcast(merge2)
    print(profit)

    shipping = shipping_costs(merge2)
    print(shipping.head())

    boxes = boxes_required(merge2, 'Number of products sold')
    print(boxes.head())

    low_20 = below_20_stock(merge2, 'Stock levels')
    print(low_20.head())
    
    log_analysis(merge2, total, low_stock)

# Select October's Glyxin record.
    material_to_order = matched_balance_main.loc[
        (matched_balance_main["month"] == "oct 2026")
        & (matched_balance_main["Material name"] == "Glyxin")
    ].copy()

# Give this material a stable identifier for supplier matching.
    material_to_order["SKU"] = "GLYXIN"

# Practice assumption:
# Next month's usage equals October's issued quantity.
# No safety stock or incoming orders included.
    material_to_order["Quantity to order"] = (
        material_to_order["Issued quantity"]
        - material_to_order["Closing quantity"]
    ).clip(lower=0)

    material_restock = material_to_order.loc[
        material_to_order["Quantity to order"] > 0,
        ["SKU", "Quantity to order"],
    ]
    print(material_restock)

    material_offers = read_fact_csv(MATERIAL_OFFERS)

#This uses the same set difference concept you practised when validating table relationships    
    missing_offers = (
        set(material_restock["SKU"])
        - set(material_offers["SKU"])
    )
    if missing_offers:
        raise ValueError(f"No supplier offers for: {missing_offers}")

#    options_to_choose = options(products, suppliers, logistics)
#    print(options_to_choose.head())

#    rstk = restock(low_20, 'Stock levels')
#    print(rstk.head()) 

#    optiz = optimize(options_to_choose, rstk, budget=10000)
#    print(optiz)

    if material_restock.empty:
        print("No purchase required under this scenario.")
    else:
        material_budget = float(
            input("Enter the material purchasing budget in VND: ")
        )
        material_offers = material_offers.loc[material_offers["SKU"].isin(material_restock["SKU"])].copy()

        # Practice assumptions—not confirmed supplier terms.
        material_offers["Shipping cost"] = (
            material_offers["Shipping cost"].fillna(0)
        )

        material_offers["Holding cost"] = (
            material_offers["Holding cost"].fillna(0)
        )

        material_offers["Minimum order quantity"] = (
            material_offers["Minimum order quantity"].fillna(0)
        )

        # For missing maximums, use the most the budget could buy.
        affordable_quantity = (
            material_budget
            // material_offers["Per-unit purchase cost"]
        )

        material_offers["Max capacity"] = (
            material_offers["Max capacity"]
            .fillna(affordable_quantity)
        )

        material_result = optimize(
            material_offers,
            material_restock,
            budget=material_budget,
        )

        print(material_result.loc[
            material_result["Optimized order"] > 0
        ])

if __name__ == "__main__":
    main()

