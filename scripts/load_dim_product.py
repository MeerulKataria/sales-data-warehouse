def load_dim_product(cursor):

    print("Loading Product Dimension...")

    # Create table
    with open("sql/ddl/create_dim_product.sql", "r") as file:
        cursor.execute(file.read())

    # Load dimension
    cursor.execute("""
        INSERT INTO dim_product
        (
            product_id,
            product_name,
            category,
            sub_category
        )

        SELECT
            product_id,
            MIN(product_name),
            MIN(category),
            MIN(sub_category)

        FROM stg_orders

        GROUP BY product_id;

    """)

    print("✅ Product Dimension loaded successfully!")