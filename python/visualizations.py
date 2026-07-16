from data_loader import load_data

df = load_data()
# -----------------------------------
# Create output folder if it doesn't exist
# -----------------------------------

output_folder = os.path.join(current_dir, "..", "charts")

os.makedirs(output_folder, exist_ok=True)

# -----------------------------------
# Sales by Category
# -----------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

bars = plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)

# Add values on top of bars

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "sales_by_category.png"),
    dpi=300
)

plt.show()


# -----------------------------------
# Monthly Revenue Trend
# -----------------------------------

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "monthly_revenue_trend.png"),
    dpi=300
)

plt.show()

# -----------------------------------
# Profit by Category
# -----------------------------------

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))

plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title("Profit by Category")

plt.xlabel("Category")

plt.ylabel("Profit")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "profit_by_category.png"),
    dpi=300
)

plt.show()

# -----------------------------------
# Sales by Segment
# -----------------------------------

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,6))

plt.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%"
)

plt.title("Sales by Customer Segment")

plt.savefig(
    os.path.join(output_folder, "sales_by_segment.png"),
    dpi=300
)

plt.show()


# -----------------------------------
# Profit by Region
# -----------------------------------

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))

plt.barh(
    region_profit.index,
    region_profit.values
)

plt.title("Profit by Region")

plt.xlabel("Profit")

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "profit_by_region.png"),
    dpi=300
)

plt.show()