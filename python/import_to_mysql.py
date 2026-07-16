import pandas as pd
from sqlalchemy import create_engine

# Read the Excel file
df = pd.read_excel(r"C:\Users\aadit\Documents\BDIS\data\superstore_clean.xlsx")

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:bdis123@localhost:3306/bdis")

# Upload data
df.to_sql(
    name="superstore",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data imported successfully!")