# ☕ Coffee Market Analytics Dashboard

An end-to-end Data Analytics project built using **Python, PostgreSQL, SQL, Streamlit, and Plotly** to analyze global coffee consumption and production trends.

This project was completed as part of the **Nium Data Analytics Case Study Assignment**.

---

# 📌 Project Overview

ACME Baristas plans to expand into three international markets.

Using publicly available datasets, this project builds a complete analytics pipeline—from data cleaning and database creation to interactive dashboard development—to identify the most promising markets for expansion.

The project demonstrates the complete analytics workflow expected from a Data Analyst.

---

# 🎯 Business Objectives

The dashboard answers the following business questions:

* Which three markets should ACME Baristas enter to maximize its customer base?
* Is this the right time to enter the coffee market?
* What opportunities and risks exist for international expansion?

---

# 🛠 Tech Stack

* Python
* Pandas
* PostgreSQL
* SQL
* Streamlit
* Plotly
* GitHub

---

# 📂 Project Structure

```
coffee-market-analytics/

│
├── dashboard/
│     └── app.py
│
├── data/
│     ├── raw/
│     └── processed/
│
├── database/
│     └── coffee_market.sql
│
├── notebooks/
│     └── 01_data_exploration.ipynb
│
├── sql/
│     ├── 01_market_summary.sql
│     ├── 02_top10_markets.sql
│     └── 03_market_trends.sql
│
├── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dashboard Preview

## Complete Dashboard

![Dashboard](images/dashboard_overview.png)

---

## KPI Overview

![KPI Cards](images/kpi_cards.png)

---

## Global Coffee Consumption Trend

![Market Trend](images/market_trend_year_by_year.png)

---

## Top Coffee Consuming Markets

![Top Markets](images/top10_markets.png)

---

## Top Coffee Producing Countries

![Production](images/production_graph.png)

---

## Coffee Market Activity Distribution

![Activity Distribution](images/activity_distribution.png)

---

## Global Coffee Consumption Map

![World Map](images/world_map.png)

---

## Executive Summary

![Business Insights](images/business_insights.png)

---

# 📈 Key Insights

### Highest Coffee Consumer

European Union

41,211 Thousand Bags

---

### Highest Coffee Producer

Brazil

65,000 Thousand Bags

---

### Countries Covered

93 Countries

---

### Recommended Markets

🥇 Brazil

🥈 United States

🥉 Japan

These markets were selected because of:

* Strong domestic coffee demand
* Large customer base
* Mature coffee ecosystem
* High long-term market potential

---

# 🗄 Database

The cleaned dataset was stored in PostgreSQL.

Database dump included:

```
database/
└── coffee_market.sql
```

---

# 📝 SQL Queries Included

The repository contains SQL transformation queries used during analysis.

* Market Summary
* Top 10 Coffee Markets
* Global Market Trends

Located in:

```
sql/
```

---

# ▶️ How to Run

## 1 Clone Repository

```bash
git clone https://github.com/itz-akash/coffee-market-analytics.git
```

---

## 2 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3 Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📚 Datasets Used

* USDA Coffee Market Dataset
* World Bank Population Dataset
* Country Codes Dataset

---

# 💡 Challenges Faced

* Matching country names across three independent datasets
* Handling missing values and inconsistent country codes
* Designing a clean PostgreSQL schema
* Building an interactive dashboard entirely using Python libraries
* Selecting meaningful business KPIs from multiple coffee market attributes

---

# 📌 Assumptions

* Country names were standardized before merging.
* Population values were assumed to represent the latest available record.
* Coffee consumption values are reported in thousand bags as provided by the USDA dataset.
* Market recommendations are based on available historical data.

---

# 🚀 Future Improvements

If additional time and more recent data were available, the project could be extended with:

* Sales forecasting using Machine Learning
* Coffee demand prediction
* Profitability analysis
* Market segmentation
* Time-series forecasting
* Interactive drill-down dashboards
* Automated ETL pipeline

---

# 📅 Dataset Limitation

The latest publicly available dataset used for this project contains limited information beyond 2024.

If complete 2025 market data had been available, additional analyses such as year-over-year growth, demand forecasting, and more impactful business recommendations could have been developed.

This limitation comes from the source data rather than the implementation of the analytics pipeline.

---

# 👨‍💻 Reflection

### Design Choices

The project follows a complete analytics workflow consisting of:

* Data Cleaning using Python
* Data Integration using Pandas
* PostgreSQL Database Creation
* SQL Transformations
* Interactive Streamlit Dashboard
* Business Recommendation Generation

This approach keeps the project modular, reproducible, and easy to extend.

---

### Challenges

The most significant challenge was combining three datasets that used different country names and codes. Standardizing these values before merging ensured accurate analysis and visualization.

---

### Additional Data That Would Strengthen Insights

* Coffee pricing
* Import/export revenue
* Consumer spending
* GDP
* Inflation
* Retail coffee sales
* Number of coffee shops
* Coffee consumption per capita

These datasets would enable more comprehensive market opportunity analysis.

---

# 👤 Author

**Akash Dubey**

Data Analyst | Python | SQL | PostgreSQL | Streamlit | Plotly

GitHub:
https://github.com/itz-akash

---

⭐ If you found this project useful, feel free to star the repository.
