def load_dim_customer(cursor):

    print("Loading Customer Dimension...")

    # Create table
    with open("sql/ddl/create_dim_customer.sql", "r") as file:
        cursor.execute(file.read())

    # Load customer dimension
    cursor.execute("""
        INSERT INTO dim_customer
        (
            customer_id,
            customer_name,
            segment
        )
        SELECT DISTINCT
            customer_id,
            customer_name,
            segment
        FROM stg_orders
        ORDER BY customer_id;
    """)

    print("✅ Customer Dimension loaded successfully!")