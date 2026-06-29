# ☕ Coffee Market Analytics Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Dashboard-red?style=for-the-badge&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blueviolet?style=for-the-badge&logo=plotly)

## End-to-End Coffee Market Analytics using Python, PostgreSQL, SQL, Streamlit & Plotly

Built as part of the **Nium Data Analytics Case Study Assignment**

### 🌐 Live Dashboard

https://coffee-market-analytics-akash.streamlit.app/

</div>

---

# 📖 Table of Contents

- Project Overview
- Business Problem
- Dashboard Preview
- Dashboard Features
- Technology Stack
- Project Structure
- Installation
- Dashboard Walkthrough
- Business Questions & Answers
- Key Insights
- PostgreSQL Database
- SQL Queries
- Datasets Used
- Challenges
- Assumptions
- Future Improvements
- Dataset Limitation
- Reflection
- Conclusion
- Author

---

# 📌 Project Overview

Coffee consumption continues to grow across the globe, creating significant opportunities for international coffee chains.

This project presents an end-to-end analytics solution developed to help **ACME Baristas** identify the most suitable global markets for expansion using publicly available coffee production, consumption, population, and country code datasets.

The project demonstrates a complete analytics workflow including:

- Data Collection
- Data Cleaning
- Data Integration
- PostgreSQL Database Design
- SQL Transformation Queries
- Interactive Streamlit Dashboard
- Business Recommendations

---

# 🎯 Business Problem

ACME Baristas plans to launch its coffee chain in three new international markets.

The objective of this project was to answer the following business questions:

- Which three markets should ACME Baristas enter to maximize its customer base?
- Does the available data suggest this is a good time to expand?
- What opportunities and risks should the company consider?
- Which countries currently have the strongest coffee ecosystem?

The final recommendations are based on coffee production, domestic consumption, population, historical trends, and market maturity.

---

# 📊 Dashboard Preview

## Dashboard Overview

![Dashboard Overview](images/dashboard_overview.png)

---

## KPI Cards

![KPI Cards](images/kpi_cards.png)

---

## Global Coffee Consumption Trend

![Trend](images/market_trend_year_by_year.png)

---

## Top Coffee Markets

![Top Markets](images/top10_markets.png)

---

## Top Coffee Producing Countries

![Production](images/production_graph.png)

---

## Coffee Market Activity Distribution

![Distribution](images/activity_distribution.png)

---

## Global Coffee Consumption Map

![World Map](images/world_map.png)

---

## Business Insights

![Business Insights](images/business_insights.png)

---

## Final Merged Dataset

The final analytical dataset was created by integrating:

- USDA Coffee Dataset
- World Bank Population Dataset
- Country Codes Dataset

using Python and Pandas before loading into PostgreSQL.

![Merged Dataset](images/Final_Merged.png)

---
# 🚀 Dashboard Features

The interactive Streamlit dashboard provides business users with a comprehensive view of the global coffee market through dynamic visualizations and KPIs.

### Features

- ✅ Interactive Market Year Filter
- ✅ KPI Cards
- ✅ Top 10 Coffee Consuming Countries
- ✅ Top Coffee Producing Countries
- ✅ Global Coffee Consumption Trend
- ✅ Coffee Market Activity Distribution
- ✅ Interactive World Consumption Map
- ✅ Executive Business Summary
- ✅ Download Filtered Dataset
- ✅ View Raw Dataset
- ✅ Business Recommendations

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Cleaning & ETL |
| Pandas | Data Manipulation |
| PostgreSQL | Database Management |
| SQL | Business Analysis |
| Streamlit | Dashboard Development |
| Plotly | Interactive Visualizations |
| GitHub | Version Control & Project Hosting |

---

# 📂 Project Structure

```text
coffee-market-analytics/

│
├── dashboard/
│      app.py
│
├── data/
│      raw/
│      processed/
│
├── database/
│      coffee_market.sql
│
├── notebooks/
│      01_data_exploration.ipynb
│
├── sql/
│      01_market_summary.sql
│      02_top10_markets.sql
│      03_market_trends.sql
│
├── images/
│      dashboard_overview.png
│      kpi_cards.png
│      market_trend_year_by_year.png
│      top10_markets.png
│      production_graph.png
│      activity_distribution.png
│      world_map.png
│      business_insights.png
│      Final_Merged.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/itz-akash/coffee-market-analytics.git
```

Move into the project

```bash
cd coffee-market-analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Dashboard Walkthrough

The dashboard enables interactive exploration of global coffee market data through multiple visualizations.

It provides:

- Market Year Selection
- Country-wise Domestic Consumption
- Coffee Production Analysis
- Historical Consumption Trend
- Coffee Activity Distribution
- Global Coffee Consumption Map
- Executive Business Insights

The dashboard also allows users to download filtered data for further analysis.

---

# 📌 Business Questions & Answers

## 1️⃣ Which three markets would you recommend to maximize the client base, and why?

Based on the analysis of coffee consumption, production capacity, population, and market maturity, the recommended expansion markets are:

### 🇧🇷 Brazil

- World's largest coffee producer
- Strong domestic consumption
- Well-established coffee ecosystem
- Excellent long-term market stability

### 🇺🇸 United States

- One of the world's largest coffee-consuming markets
- Large customer base
- Strong purchasing power
- Mature specialty coffee industry

### 🇯🇵 Japan

- Stable coffee demand
- High disposable income
- Growing premium coffee segment
- Well-developed retail infrastructure

---

## 2️⃣ Does the data suggest this is a good time to enter the coffee market?

**Yes.**

Historical coffee consumption demonstrates consistent long-term demand across major international markets.

The analysis indicates that coffee remains one of the most resilient consumer products, making expansion into high-demand regions a promising opportunity.

Although the latest publicly available dataset contains limited information for the most recent market period, the historical trends strongly support continued market growth.

---

## 3️⃣ What opportunities and risks exist?

### Opportunities

- Increasing global coffee consumption
- Rising specialty coffee culture
- Large addressable consumer markets
- Premium product opportunities
- Strong international demand
- Long-term market growth

### Risks

- Intense competition from established brands
- Coffee bean price fluctuations
- Climate-related production risks
- Supply chain disruptions
- Dependence on publicly available historical datasets

---

## 4️⃣ Which countries have the strongest coffee ecosystem?

Considering coffee production, domestic consumption, market maturity, and global importance, the strongest coffee ecosystems are:

| Country | Strength |
|----------|----------|
| 🇧🇷 Brazil | Largest coffee producer with strong domestic demand |
| 🇺🇸 United States | Largest premium coffee consumer market |
| 🇯🇵 Japan | Mature specialty coffee market |
| 🇪🇺 European Union | Highest domestic coffee consumption in the dataset |
| 🇻🇳 Vietnam | Major global coffee producer and exporter |

These countries demonstrate strong supply chains, established coffee industries, and significant consumer demand, making them strategically important in the global coffee market.

---

# 📊 Key Insights

## Highest Coffee Consumer

**European Union**

- Highest domestic coffee consumption in the available dataset
- Mature coffee market with consistent long-term demand

---

## Largest Coffee Producer

**Brazil**

- World's largest coffee producer
- Strong export capabilities
- Large domestic consumer base

---

## Countries Covered

- **93 Countries**
- Multiple years of historical market data
- Integrated with World Bank population statistics

---

## Coffee Market Indicators

The dashboard analyzes **19 coffee market attributes**, including:

- Production
- Domestic Consumption
- Imports
- Exports
- Beginning Stocks
- Ending Stocks
- Total Distribution
- And additional market indicators

---

# 🗄 PostgreSQL Database

The cleaned and integrated dataset was imported into PostgreSQL to support structured querying and analytical reporting.

The repository contains:

```text
database/
└── coffee_market.sql
```

The SQL dump can be restored using PostgreSQL or pgAdmin.

---

# 📝 SQL Transformation Queries

Business analysis was performed using PostgreSQL SQL queries.

Included SQL files:

```text
sql/

01_market_summary.sql

02_top10_markets.sql

03_market_trends.sql
```

These queries support:

- Market summary analysis
- Top consuming countries
- Historical trend analysis

---

# 📚 Datasets Used

This project combines three public datasets.

### USDA Coffee Dataset

Contains:

- Coffee Production
- Imports
- Exports
- Domestic Consumption
- Stocks
- Total Distribution

---

### World Bank Population Dataset

Provides annual population estimates for countries worldwide.

---

### Country Codes Dataset

Provides standardized ISO country codes used for joining datasets accurately.

---

# 💡 Challenges Faced

Several data engineering challenges were encountered during the project:

- Country name inconsistencies across datasets
- ISO code mismatches
- Missing population values
- Duplicate records
- Data standardization
- Integrating three independent public datasets

These issues were addressed through Python preprocessing, data validation, and careful country name normalization before loading the final dataset into PostgreSQL.

---

# 📌 Assumptions

The following assumptions were made during analysis:

- Country names were standardized before merging.
- Population values represent the latest available estimates.
- Domestic Consumption was used as the primary indicator of market demand.
- Public datasets accurately represent historical market conditions.

---

# 🚀 Future Improvements

Given additional time and richer datasets, this project could be extended by implementing:

- Machine Learning demand forecasting
- Time-series forecasting
- Coffee price trend analysis
- Customer segmentation
- Retail sales analytics
- Revenue forecasting
- Automated ETL pipelines
- Cloud-hosted PostgreSQL integration
- Real-time dashboard updates

---

# 📅 Dataset Limitation

The publicly available USDA Coffee dataset contains limited information for the most recent market period and does not include complete data for 2025.

If newer datasets were available, the project could include:

- Year-over-Year Growth Analysis
- Demand Forecasting
- Market Forecasting
- Predictive Analytics
- More comprehensive strategic recommendations

This limitation is due to the availability of public source data rather than the implementation of the analytics solution.

---

# 📝 Reflection

## Design Choices

The solution follows a modular analytics architecture using:

- Python for ETL
- PostgreSQL for structured storage
- SQL for business transformations
- Streamlit for visualization

This design improves maintainability, scalability, and reproducibility.

---

## Challenges

The most significant challenge was integrating three independent datasets with inconsistent country names and missing identifiers.

Data standardization and validation ensured accurate joins and reliable analytical outputs.

---

## Additional Data That Would Strengthen the Analysis

Future analyses would benefit from:

- Coffee Prices
- GDP
- Inflation
- Retail Sales
- Coffee Shop Density
- Consumer Spending
- Per Capita Coffee Consumption
- Import & Export Revenue
- Consumer Preference Data

These datasets would support more advanced forecasting and profitability analysis.

---

# 🏁 Conclusion

This project demonstrates a complete end-to-end analytics workflow beginning with raw public datasets and ending with actionable business insights.

The project successfully showcases:

- Python Data Cleaning
- Data Integration
- PostgreSQL Database Design
- SQL Transformations
- Interactive Streamlit Dashboard
- Business Storytelling
- Data Visualization

Based on the analysis, **Brazil**, **United States**, and **Japan** are recommended as the most promising markets for ACME Baristas due to their strong coffee demand, market maturity, and long-term growth potential.

---

# 👨‍💻 Author

## Akash Dubey

**Data Analyst**

### Skills

Python • SQL • PostgreSQL • Streamlit • Plotly • Pandas • Data Visualization • ETL

### 🌐 Live Dashboard

https://coffee-market-analytics-akash.streamlit.app/
---

# 🙏 Acknowledgements

This project was developed as part of the **Nium Data Analytics Case Study Assignment** using publicly available datasets from:

- USDA Foreign Agricultural Service (Coffee Dataset)
- World Bank (Population Dataset)
- OpenDataSoft (Country Codes Dataset)

Special thanks to these organizations for providing open data that made this analysis possible.

---

⭐ If you found this project interesting, please consider giving it a star on GitHub!
