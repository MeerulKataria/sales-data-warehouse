def load_dim_product(cursor):

    print("Loading Product Dimension...")

    # Create table
    with open("sql/ddl/create_dim_product.sql", "r") as file:
        cursor.execute(file.read())

    # Insert data
    cursor.execute("""
        INSERT INTO dim_product
        (
            product_id,
            category,
            sub_category,
            product_name
        )
        SELECT DISTINCT
            product_id,
            category,
            sub_category,
            product_name
        FROM stg_orders;
    """)

    print("✅ Product Dimension loaded.")