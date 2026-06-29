import os
import sys
import psycopg2

# Allow importing modules from the scripts folder
sys.path.append(os.path.dirname(__file__))

from load_stage import load_stage
from load_dim_customer import load_dim_customer
from load_dim_product import load_dim_product
from load_dim_date import load_dim_date


def main():

    try:
        print("=" * 60)
        print(" SALES DATA WAREHOUSE ETL PIPELINE ")
        print("=" * 60)

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="sales_dw",
            user="postgres",
            password="meerul1234",
            port="5432"
        )

        cursor = conn.cursor()

        print("✅ Connected to PostgreSQL\n")

        # -------------------------
        # Load Stage
        # -------------------------
        load_stage(cursor)
        conn.commit()

        # -------------------------
        # Load Customer Dimension
        # -------------------------
        load_dim_customer(cursor)
        conn.commit()

        # -------------------------
        # Load Product Dimension
        # -------------------------
        load_dim_product(cursor)
        conn.commit()

        print("\n🎉 Customer & Product Dimension ETL Completed Successfully!")

        # Close connection
        cursor.close()
        conn.close()

        print("✅ PostgreSQL connection closed.")
        # ------------------------
        # # Load Date Dimension
        # # -------------------------
        # load_dim_date(cursor)
        # conn.commit()

    except Exception as e:
        print("\n❌ ETL Failed")
        print(e)


if __name__ == "__main__":
    main()