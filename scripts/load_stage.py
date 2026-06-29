import pandas as pd


def load_stage(cursor):

    print("Loading staging table...")

    # Read cleaned dataset
    df = pd.read_csv(
        "data/processed/stg_orders.csv",
        parse_dates=["order_date", "ship_date"]
    )

    # Create staging table
    with open("sql/ddl/create_stg_orders.sql", "r") as file:
        cursor.execute(file.read())

    # Insert rows
    for _, row in df.iterrows():

        cursor.execute("""
            INSERT INTO stg_orders (
                row_id,
                order_id,
                order_date,
                ship_date,
                ship_mode,
                customer_id,
                customer_name,
                segment,
                country,
                city,
                state,
                postal_code,
                region,
                product_id,
                category,
                sub_category,
                product_name,
                sales,
                quantity,
                discount,
                profit
            )
            VALUES (
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s
            )
        """, tuple(row))

    print("✅ Stage loaded.")