def load_fact_sales(cursor):

    print("Loading Fact Sales...")

    # Create table
    with open("sql/ddl/create_fact_sales.sql", "r") as file:
        cursor.execute(file.read())

    # Load fact table
    cursor.execute("""
        INSERT INTO fact_sales
        (
            customer_key,
            product_key,
            date_key,
            sales,
            quantity,
            discount,
            profit
        )

        SELECT

            c.customer_key,

            p.product_key,

            d.date_key,

            s.sales,

            s.quantity,

            s.discount,

            s.profit

        FROM stg_orders s

        JOIN dim_customer c
            ON s.customer_id = c.customer_id

        JOIN dim_product p
            ON s.product_id = p.product_id

        JOIN dim_date d
            ON s.order_date = d.full_date;
    """)

    print("✅ Fact Sales loaded successfully!")