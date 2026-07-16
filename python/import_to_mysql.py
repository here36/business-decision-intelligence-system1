import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel(r"C:\Users\aadit\Documents\BDIS\data\superstore_clean.xlsx")

# Convert Excel serial numbers to real dates
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    unit="D",
    origin="1899-12-30"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    unit="D",
    origin="1899-12-30"
)

engine = create_engine("mysql+pymysql://root:bdis123@localhost:3306/bdis")

df.to_sql(
    "superstore",
    con=engine,
    if_exists="replace",
    index=False
)

print("Imported Successfully!")