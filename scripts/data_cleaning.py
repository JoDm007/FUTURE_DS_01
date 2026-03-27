# This script will handle data preprocessing and cleaning operations
#Data cleaning script for Superstore sales analysis
#Author: Joseph DATE-MASSE

import pandas as pd

def clean_sales_data(input_path, output_path):
    """Nettoie les données de ventes"""
    df = pd.read_csv(input_path)

    #  Data Cleaning
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # Creation of util columns
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['YearMonth'] = df['Order Date'].dt.to_period('M')
    df['Shipping_Days'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

    # Audit of Extreme Discounts
    print(f"\n📊 Audit des données :")
    print(f"   - Ventes négatives : {(df['Sales'] < 0).sum()}")
    print(f"   - Profits négatifs : {(df['Profit'] < 0).sum()}")
    print(f"   - Discounts > 50% : {(df['Discount'] > 0.5).sum()}")

    # Droping of duplicates values
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"\n🗑️ Doublons supprimés : {duplicates}")
    else:
        print("\n✅ Aucun doublon trouvé")

    # Save the cleaned dataset to a new CSV file.
    df.to_csv(output_path, index=False)
    print(f"✅Data cleaned and saved successfully! {output_path}")
    return df

if __name__ == "__main__":
    clean_sales_data(
        input_path="../data/raw/Sample - Superstore.csv",
        output_path="../data/processed/cleaned_superstore.csv"
    )