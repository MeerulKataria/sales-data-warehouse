import pandas as pd
import psycopg2

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="sales_dw",
        user="postgres",
        password="meerul1234",
        port="5432"
    )

    print("✅ Connected to PostgreSQL successfully!")

    # Read cleaned dataset
    df = pd.read_csv(
        "data/processed/stg_orders.csv",
        parse_dates=["order_date", "ship_date"]
    )

    print(df.head())
    print(df.shape)

    # Create cursor
    cursor = conn.cursor()

    # Read SQL file
    with open("sql/ddl/create_stg_orders.sql", "r") as file:
        sql_script = file.read()

    # Execute SQL
    cursor.execute(sql_script)
    conn.commit()

    print("✅ stg_orders table created successfully!")

    # Insert data into stg_orders
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

    conn.commit()

    print("✅ All data inserted successfully!")

    cursor.close()
    conn.close()

except Exception as e:
    print(e)