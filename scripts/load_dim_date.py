import pandas as pd


def load_dim_date(cursor):

    print("Loading Date Dimension...")

    # ==============================
    # Create Date Dimension Table
    # ==============================
    with open("sql/ddl/create_dim_date.sql", "r") as file:
        cursor.execute(file.read())

    # ==============================
    # Read staging data
    # ==============================
    df = pd.read_csv(
        "data/processed/stg_orders.csv",
        parse_dates=["order_date"]
    )

    # ==============================
    # Build Date Dimension
    # ==============================
    date_df = pd.DataFrame()

    date_df["full_date"] = df["order_date"].drop_duplicates()

    date_df = date_df.sort_values("full_date")

    date_df["date_key"] = date_df["full_date"].dt.strftime("%Y%m%d").astype(int)
    date_df["day"] = date_df["full_date"].dt.day
    date_df["month"] = date_df["full_date"].dt.month
    date_df["month_name"] = date_df["full_date"].dt.month_name()
    date_df["quarter"] = date_df["full_date"].dt.quarter
    date_df["year"] = date_df["full_date"].dt.year
    date_df["weekday"] = date_df["full_date"].dt.day_name()

    # ==============================
    # Reorder columns to match SQL
    # ==============================
    date_df = date_df[
        [
            "date_key",
            "full_date",
            "day",
            "month",
            "month_name",
            "quarter",
            "year",
            "weekday"
        ]
    ]

    # ==============================
    # Insert into dim_date
    # ==============================
    for _, row in date_df.iterrows():

        cursor.execute("""
            INSERT INTO dim_date
            (
                date_key,
                full_date,
                day,
                month,
                month_name,
                quarter,
                year,
                weekday
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s
            )
        """, tuple(row))

    print("✅ Date Dimension loaded successfully!")