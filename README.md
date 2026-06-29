# ☕ Coffee Market Analytics Dashboard

## 📌 Project Overview

This project analyzes global coffee market data to help **ACME Baristas** identify the best international markets for expansion.

The project integrates coffee consumption, world population, and country code datasets into a single PostgreSQL database. SQL queries are used to perform business analysis, while a Streamlit dashboard provides interactive visualizations.

---

## 🎯 Business Objective

ACME Baristas plans to launch coffee stores in three new international markets.

This analysis answers:

* Which three markets should ACME enter?
* Is this the right time to enter the coffee market?
* What opportunities and risks exist in different markets?

---

## 🛠 Tech Stack

* Python
* Pandas
* PostgreSQL
* SQL
* Streamlit
* Plotly
* GitHub

---

## 📂 Project Structure

```text
coffee-market-analytics/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── coffee_market.sql
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── sql/
│   ├── 01_market_summary.sql
│   ├── 02_top10_markets.sql
│   └── 03_market_trends.sql
│
├── images/
│
├── requirements.txt
│
└── README.md
```
## 📊 Dashboard Features

The Streamlit dashboard includes:

* KPI Cards

  * Number of Countries
  * Total Domestic Consumption
  * Total Population
  * Number of Coffee Market Activities

* Interactive Year Filter

* Top 10 Coffee Consuming Countries

* Top Coffee Producing Countries

* Coffee Market Activity Distribution (Pie Chart)

* Global Coffee Consumption Map

* Business Insights Summary

* Download Filtered Dataset (CSV)

* Raw Dataset Viewer

---

## 📁 Datasets Used

### 1. Coffee Market Dataset

Source:
https://apps.fas.usda.gov/psdonline/app/index.html#/app/downloads

Contains:

* Country
* Market Year
* Coffee Production
* Domestic Consumption
* Imports
* Exports
* Ending Stocks
* Other coffee market indicators

---

### 2. World Population Dataset

Source:
https://data.worldbank.org/indicator/SP.POP.TOTL

Contains yearly population of each country.

---

### 3. Country Codes Dataset

Source:
https://public.opendatasoft.com/explore/dataset/countries-codes/table/

Contains:

* Country Name
* ISO3 Country Code

Used for joining datasets and creating the world map.

---

## 🗄 Database

Database Used:

PostgreSQL

Database Name:

coffee_market_db

Main Table:

coffee_market

The cleaned dataset was loaded into PostgreSQL using Python (SQLAlchemy).

---

## 📜 SQL Queries

Three SQL scripts were created:

### 01_market_summary.sql

Provides market summary by country.

### 02_top10_markets.sql

Returns the Top 10 coffee consuming countries.

### 03_market_trends.sql

Analyzes yearly domestic coffee consumption trends.

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/itz-akash/coffee-market-analytics.git
```

### 2. Navigate to the Project Folder

```bash
cd coffee-market-analytics
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser at:

```
http://localhost:8501
```

---

# 📈 Business Recommendations

Based on the analysis, the recommended markets for ACME Baristas are:

## 🇧🇷 Brazil

* Largest coffee consuming market
* Strong existing coffee culture
* High consumer demand

## 🇺🇸 United States

* Large customer base
* High purchasing power
* Mature coffee retail market

## 🇯🇵 Japan

* Stable demand
* Premium coffee segment
* High-quality specialty coffee market

---

# 📌 Key Insights

* Global coffee consumption has generally increased over recent years.
* Brazil consistently remains the largest coffee consuming market.
* Several developing countries show increasing coffee demand.
* Population growth supports future market expansion.
* Consumption trends indicate long-term growth potential.

---

# ⚠️ Risks

* Strong competition from existing coffee chains.
* Economic fluctuations affecting consumer spending.
* Differences in coffee preferences across regions.
* Supply chain and import costs.

---

# 🚀 Opportunities

* Growing specialty coffee market.
* Rising urban population.
* Increasing café culture worldwide.
* Expansion into emerging markets.

---

# 📸 Dashboard Preview

Dashboard screenshots are available in the **images/** folder.

Included screenshots:

* Dashboard Overview
* KPI Cards
* Top 10 Coffee Markets
* Production Analysis
* Market Trend
* World Consumption Map
* Business Insights
* Activity Distribution

# 📝 Reflection

## Key Design Choices

The primary goal was to build a clean, reproducible analytics pipeline that closely mirrors a real-world data analytics workflow.

Key design decisions included:

* Using **Python (Pandas)** for data cleaning, transformation, and dataset integration.
* Standardizing country names and ISO3 country codes before joining datasets to improve data quality.
* Loading the final cleaned dataset into **PostgreSQL** for structured storage and SQL-based analysis.
* Writing separate SQL scripts for reusable business transformations instead of embedding SQL directly in Python.
* Building an interactive **Streamlit dashboard** with Plotly to present insights in a user-friendly and business-focused manner.
* Organizing the repository into clearly separated folders for data, SQL, notebooks, dashboard, database, and documentation to improve maintainability.

---

## Challenges Faced

Several challenges were encountered during the project:

* Country names and ISO codes were inconsistent across the three datasets, requiring manual mapping and standardization.
* Some countries and regional entities did not have matching population records, which initially reduced the merge success rate.
* Building a reliable join across multiple public datasets required validating country mappings and handling missing values carefully.
* Configuring PostgreSQL, loading data, and integrating it with the Python pipeline required additional setup and testing.
* Developing an interactive dashboard without using drag-and-drop BI tools required implementing all visualizations programmatically using Streamlit and Plotly.

These challenges were addressed through data validation, ISO3 code mapping, manual country corrections, and iterative testing, resulting in a successful merge rate of approximately **97%**.

---

## Assumptions

The following assumptions were made during the analysis:

* Domestic Consumption was considered the primary indicator of market demand.
* Population values from the World Bank dataset were treated as the most reliable available estimates.
* Countries with missing or unavailable population data were excluded only where required.
* Coffee consumption values are reported in **1000 (60 KG) Bags**, as provided by the USDA dataset.
* Recommendations are based on the available historical data and should not be interpreted as financial forecasts.

---

## If I Had More Time

Given additional time and access to richer datasets, I would further enhance this project by:

* Deploying the Streamlit dashboard to a public cloud platform.
* Building forecasting models to predict future coffee demand.
* Adding advanced KPIs such as per-capita coffee consumption, growth rates, and market penetration.
* Incorporating additional economic indicators including GDP per capita, disposable income, inflation, and retail coffee spending.
* Comparing market opportunities against competitor presence and café density.

**Note:** The publicly available dataset used for this assignment contained limited information for the most recent market period, which restricted more advanced trend forecasting and forward-looking analysis. With a more complete and up-to-date 2025 dataset, I would have developed richer predictive models, stronger market forecasts, and more impactful strategic recommendations.

---

## Additional Data That Would Strengthen the Analysis

The following datasets would improve the quality of business recommendations:

* GDP per capita
* Consumer purchasing power
* Coffee retail sales revenue
* Coffee shop density by country
* Import and export tariffs
* Inflation rates
* Urban population growth
* Competitor presence (e.g., Starbucks, Costa Coffee, Tim Hortons)
* Consumer preference and specialty coffee trends

---

# 👨‍💻 Author

**Akash Dubey**

Data Analyst | Python | SQL | PostgreSQL | Streamlit | Plotly

GitHub: https://github.com/itz-akash

---

# ⭐ Thank You

Thank you for reviewing this project.

This repository demonstrates a complete end-to-end data analytics workflow, including:

* Data Collection
* Data Cleaning & Transformation
* Multi-source Data Integration
* PostgreSQL Database Design
* SQL Analysis
* Interactive Streamlit Dashboard
* Business Insights & Market Recommendations

This project was developed as part of the **Nium Data Analytics Case Study Assignment**.