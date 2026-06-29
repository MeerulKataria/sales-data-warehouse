def load_dim_date(cursor):

    print("Loading Date Dimension...")

    # Create table
    with open("sql/ddl/create_dim_date.sql", "r") as file:
        cursor.execute(file.read())

    # Insert data
    cursor.execute("""
        INSERT INTO dim_date
        (
            order_date,
            year,
            quarter,
            month,
            month_name,
            day
        )
        SELECT DISTINCT
            order_date,
            EXTRACT(YEAR FROM order_date),
            EXTRACT(QUARTER FROM order_date),
            EXTRACT(MONTH FROM order_date),
            TO_CHAR(order_date, 'Month'),
            EXTRACT(DAY FROM order_date)
        FROM stg_orders;
    """)

    print("✅ Date Dimension loaded.")