# Analysis functions for Superstore sales data
# This script contains reusable functions for data analysis and visualization
#Autor: Joseph DATE-MASSE

import pandas as pd

def get_global_metric(df):
    """ Calcule des metriques globale"""
    return {
        'total_revenue': df['Sales'].sum(),
        'total_profit': df['Profit'].sum(),
        'avg_margin': (df['Profit'].sum()   /   df['Sales'].sum() * 100),
        'total_quantitiy': df['Quantity'].sum()
    }

def get_top_products(df, n=10):
    """Retourner les n produits les plus vendus"""
    return df.groupby('Product Name')['Sales'].sum().sort_values(ascending=Fales).head(n).reset_index()

def get_category_analysis(df):
    """Analyse par categorie"""
    return df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum'
    }).sort_values('Sales', ascending=False).reset_index()

def get_region_analysis(df):
    """Analyse par region"""
    return df.groupby('Region').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum'
    }).sort_values('Sales', ascending=False).reset_index()