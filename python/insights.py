from data_loader import load_data

df = load_data()

category_sales = df.groupby("Category")["Sales"].sum()

top_category = category_sales.idxmax()

top_category_sales = category_sales.max()

print("="*60)
print("BUSINESS INSIGHTS")
print("="*60)

print(
    f"Highest Revenue Category : {top_category}"
)

print(
    f"Revenue Generated : ₹{top_category_sales:,.2f}"
)
# -----------------------------------
# Most Profitable Category
# -----------------------------------

category_profit = df.groupby("Category")["Profit"].sum()

top_profit_category = category_profit.idxmax()

top_profit = category_profit.max()

print("\nMost Profitable Category :", top_profit_category)
print(f"Profit Generated : ₹{top_profit:,.2f}")
# -----------------------------------
# Best Performing Region
# -----------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

best_region = region_sales.idxmax()

best_region_sales = region_sales.max()

print("\nBest Performing Region :", best_region)
print(f"Revenue : ₹{best_region_sales:,.2f}")

# -----------------------------------
# Best Customer Segment
# -----------------------------------

segment_sales = df.groupby("Segment")["Sales"].sum()

best_segment = segment_sales.idxmax()

best_segment_sales = segment_sales.max()

print("\nBest Customer Segment :", best_segment)
print(f"Revenue : ₹{best_segment_sales:,.2f}")

# -----------------------------------
# Lowest Profit Category
# -----------------------------------

lowest_profit_category = category_profit.idxmin()

lowest_profit = category_profit.min()

print("\nLowest Profit Category :", lowest_profit_category)
print(f"Profit : ₹{lowest_profit:,.2f}")