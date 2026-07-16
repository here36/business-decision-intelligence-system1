from data_loader import load_data

df = load_data()

# ----------------------------
# BUSINESS KPIs
# ----------------------------

total_revenue = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = len(df)

unique_customers = df["Customer ID"].nunique()

loss_products = df[df["Profit"] < 0]["Product Name"].nunique()
# ----------------------------
# CATEGORY ANALYSIS
# ----------------------------

category_sales = df.groupby("Category")["Sales"].sum()

category_profit = df.groupby("Category")["Profit"].sum()

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit)

# ----------------------------
# REGION ANALYSIS
# ----------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\n========== SALES BY REGION ==========")
print(region_sales)

# ----------------------------
# CUSTOMER SEGMENT ANALYSIS
# ----------------------------

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\n========== SALES BY SEGMENT ==========")
print(segment_sales)
# ----------------------------
# PRINT RESULTS
# ----------------------------

print("="*50)
print(" BUSINESS DECISION INTELLIGENCE SYSTEM ")
print("="*50)

print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Profit       : ₹{total_profit:,.2f}")
print(f"Total Orders       : {total_orders}")
print(f"Unique Customers   : {unique_customers}")
print(f"Loss Products      : {loss_products}")

print("="*50)