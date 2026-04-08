# KPI calculations for Superstore analysis
#Autor: Joseph DATE-MASSE

import pandas as pd


def calculate_business_kpis(df):
    """Calcule les KPIs business pour le rapport."""

    kpis = {}

    # === REVENUS ===
    kpis["total_revenue"] = df["Sales"].sum()
    kpis["avg_order_value"] = df["Sales"].mean()
    kpis["total_orders"] = df["Order ID"].nunique()

    # === RENTABILITÉ ===
    kpis["total_profit"] = df["Profit"].sum()
    kpis["profit_margin_pct"] = (kpis["total_profit"] / kpis["total_revenue"]) * 100
    kpis["loss_making_products"] = df[df["Profit"] < 0]["Product Name"].nunique()

    # === EFFICACITÉ ===
    kpis["avg_discount"] = df["Discount"].mean() * 100
    if "Shipping_Days" in df.columns:
        kpis["avg_shipping_days"] = df["Shipping_Days"].mean()
    else:
        ship = pd.to_datetime(df["Ship Date"])
        order = pd.to_datetime(df["Order Date"])
        kpis["avg_shipping_days"] = (ship - order).dt.days.mean()

    # === SEGMENTATION ===
    kpis["top_region"] = df.groupby("Region")["Sales"].sum().idxmax()
    kpis["top_category"] = df.groupby("Category")["Sales"].sum().idxmax()

    return kpis
