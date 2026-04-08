# Superstore Sales Analysis Project

## Project Structure

This project analyzes sales data from the Sample Superstore dataset to identify key business insights and trends.

### Directory Structure

```
FUTURE_DS_01/
├── data/
│   ├── raw/                     # Original datasets
│   │   └── Sample-Superstore.csv
│   └── processed/               # Cleaned and processed data
│       └── cleaned_superstore.csv
│
├── notebooks/                   # Jupyter notebooks for analysis
│   ├── 01_data_cleaning.ipynb   # Data cleaning and preprocessing
│   ├── 02_exploratory_analysis.ipynb  # EDA and visualizations
│   └── 03_key_metrics_calculation.ipynb  # Business metrics calculation
│
├── reports/                     # Final reports and visualizations
│   ├── sales_analysis_report.md
│   └── images/                  # Generated charts and graphs
│
├── tableau/                     # Tableau dashboards
│   └── sales_dashboard.twbx
│
├── src/                     # Reusable Python scripts
│   ├── data_cleaning.py
│   ├── metrics.py
│   └── analysis_functions.py
│
├── F_DS_01_env/
├── README.md
└── requirements.txt
```

## Analysis Objectives

1. **Revenue Trends**: Analyze sales patterns over time
2. **Top-Selling Products**: Identify best-performing products
3. **High-Value Categories**: Find categories with highest revenue
4. **Regional Performance**: Compare sales across different regions

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Run notebooks in order: 01 → 02 → 03
3. View final report in `reports/` directory

## 👤 Auteur
[Joseph DATE-MASSE] - Intern Data Science & Analytics @ Future Interns
