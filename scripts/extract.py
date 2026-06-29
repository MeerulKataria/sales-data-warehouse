import pandas as pd

# File path
file_path = "data/raw/Sample - Superstore.csv"

# Read CSV
df = pd.read_csv(file_path, encoding="latin1")

# Convert column names to snake_case
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("-", "_")
)

# Convert date columns to datetime
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# ===========================================
print("=" * 50)
print("Dataset Shape")
print(df.shape)

# ===========================================
print("\n" + "=" * 50)
print("Snake Case Column Names")
print(df.columns)

# ===========================================
print("\n" + "=" * 50)
print("Data Types")
print(df.dtypes)

# ===========================================
print("\n" + "=" * 50)
print("First Five Rows")
print(df.head())
print("\n" + "=" * 50)
print("Missing Values")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("Duplicate Rows")
print(df.duplicated().sum())
print("\n" + "=" * 50)
print("Summary Statistics")
print(df.describe())
print("\n" + "=" * 50)
print("Unique Values in Important Columns")

print("Ship Modes:", df["ship_mode"].unique())
print("Segments:", df["segment"].unique())
print("Categories:", df["category"].unique())
print("Sub-Categories:", df["sub_category"].unique())
print("Regions:", df["region"].unique())
print("\n" + "=" * 50)
print("Dataset Information")
df.info()
# Create staging dataframe
staging_df = df.copy()

print("\n" + "=" * 50)
print("Created Staging DataFrame")
print(staging_df.shape)
print("\n" + "=" * 50)
print("Duplicate Rows Before Cleaning")
print(staging_df.duplicated().sum())
staging_df = staging_df.drop_duplicates()
print("\n" + "=" * 50)
print("Duplicate Rows After Cleaning")
print(staging_df.duplicated().sum())
print("\n" + "=" * 50)
print("Missing Values Before Cleaning")
print(staging_df.isnull().sum())
print("\nTotal Missing Values:")
print(staging_df.isnull().sum().sum())
# Standardize text columns
text_columns = staging_df.select_dtypes(include="object").columns

for col in text_columns:
    staging_df[col] = staging_df[col].str.strip()
    print("\n" + "=" * 50)
print("Text Columns Standardized")
print(text_columns.tolist())
print("\n" + "=" * 50)
print("Numeric Column Summary")

numeric_columns = ["sales", "quantity", "discount", "profit"]

print(staging_df[numeric_columns].describe())
print("\n" + "=" * 50)
print("Business Rule Validation")

print("Negative Sales:", (staging_df["sales"] < 0).sum())
print("Invalid Quantity:", (staging_df["quantity"] <= 0).sum())
print("Invalid Discount:", ((staging_df["discount"] < 0) | (staging_df["discount"] > 1)).sum())
print("\n" + "=" * 50)
print("Saving Cleaned Dataset...")

output_path = "data/processed/stg_orders.csv"

staging_df.to_csv(output_path, index=False)

print("Dataset saved successfully!")
print("Location:", output_path)
print("\n" + "=" * 50)
print("Verifying Saved Dataset")

verification_df = pd.read_csv(
    "data/processed/stg_orders.csv",
    parse_dates=["order_date", "ship_date"]
)

print("Verification Shape:", verification_df.shape)
print(verification_df.head())