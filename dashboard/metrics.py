def get_metrics(df):

    total_revenue = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = len(df)

    unique_customers = df["Customer ID"].nunique()

    loss_products = df[df["Profit"] < 0]["Product Name"].nunique()

    return (
        total_revenue,
        total_profit,
        total_orders,
        unique_customers,
        loss_products
    )