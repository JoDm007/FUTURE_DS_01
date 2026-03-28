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
│   ├── sales_analysis_report.pdf
│   └── images/                  # Generated charts and graphs
│       ├── revenue_trend.png
│       ├── top_products.png
│       ├── sales_by_category.png
│       ├── sales_by_region.png
│       └── dashboard_overview.png
│
├── tableau/                     # Tableau dashboards
│   └── sales_dashboard.twbx
│
├── scripts/                     # Reusable Python scripts
│   ├── data_cleaning.py
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




====================================================================
FUTURE_DS_01/
│
├── README.md                          # Présentation du projet + badges
├── requirements.txt                   # Dépendances Python
├── .gitignore                         # Fichiers à ignorer
├── LICENSE                            # Licence du projet
│
├── data/
│   ├── raw/                           # Données brutes 
│   │   └── Sample-Superstore.csv
│   ├── processed/                     # Données nettoyées
│   │   └── cleaned_superstore.csv
│   └── README.md                      # Documentation des datasets
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb         # Nettoyage & préprocessing
│   ├── 02_exploratory_analysis.ipynb  # EDA avec visualisations
│   ├── 03_key_metrics_calculation.ipynb # Calcul des KPIs
│   └── 04_insights_summary.ipynb      # Synthèse & recommandations
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py               # Fonctions de nettoyage réutilisables
│   ├── visualization.py               # Fonctions de graphiques (matplotlib/seaborn/plotly)
│   ├── metrics.py                     # Calcul des KPIs business
│   └── utils.py                       # Helpers divers
│
├── reports/
│   ├── figures/                       # Graphiques exportés (PNG/SVG)
│   │   ├── revenue_trend.png
│   │   ├── category_analysis.png
│   │   └── region_performance.png
│   └── final_report.pdf               # Rapport final 
│
├── dashboard/
│   ├── tableau/                       # Fichiers Tableau (.twbx, .twb)
│   │   ├── Superstore_Analysis.twbx
│   │   └── README_Tableau.md          # Guide d'utilisation
│   └── streamlit/                     # Optionnel: app interactive Python
│       ├── app.py
│       └── requirements.txt
│
├── docs/
│   ├── methodology.md                 # Méthodologie d'analyse
│   ├── business_questions.md          # Questions métier adressées
│   └── linkedin_posts/                # Brouillons de posts
│       ├── post1_announcement.md
│       └── post2_insights.md
│
└── tests/
    ├── test_data_cleaning.py          # Tests unitaires (optionnel mais pro)
    └── test_metrics.py
====================================================================