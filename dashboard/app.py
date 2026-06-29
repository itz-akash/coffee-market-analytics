import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="Coffee Market Analytics",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

.main-title{
    font-size:42px;
    font-weight:700;
    color:#6F4E37;
}

.subtitle{
    font-size:18px;
    color:gray;
    margin-bottom:20px;
}

div[data-testid="metric-container"]{
    background:#f8f9fa;
    border:1px solid #ddd;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 6px rgba(0,0,0,.08);
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent

    csv_path = BASE_DIR / "data" / "processed" / "coffee_market_analysis.csv"

    df = pd.read_csv(csv_path)

    return df

df = load_data()

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2935/2935307.png",
    width=90
)

st.sidebar.title("Coffee Dashboard")

st.sidebar.markdown("""
This dashboard analyses

- Coffee Consumption
- Coffee Production
- Global Markets
- Population
- Market Opportunities
""")

years = sorted(df["Market_Year"].unique())

default_year = 2024 if 2024 in years else years[-1]

selected_year = st.sidebar.selectbox(
    "Select Market Year",
    years,
    index=years.index(default_year)
)

filtered_df = df[df["Market_Year"] == selected_year]

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.markdown(
"""
<div class='main-title'>
☕ Coffee Market Analytics Dashboard
</div>

<div class='subtitle'>
ACME Baristas | Global Coffee Consumption & Production Analysis
</div>
""",
unsafe_allow_html=True
)

# -----------------------------------------------------
# KPI CALCULATIONS
# -----------------------------------------------------

countries = filtered_df["Country_Name"].nunique()

consumption = filtered_df[
    filtered_df["Attribute_Description"]=="Domestic Consumption"
]["Value"].sum()

production = filtered_df[
    filtered_df["Attribute_Description"]=="Production"
]["Value"].sum()

population = filtered_df["Population"].dropna().max()

# -----------------------------------------------------
# KPI CARDS
# -----------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "🌍 Countries",
        countries
    )

with c2:
    st.metric(
        "☕ Consumption",
        f"{consumption:,.0f}"
    )

with c3:
    st.metric(
        "🌱 Production",
        f"{production:,.0f}"
    )

with c4:
    if pd.notna(population):
        pop_display = f"{population/1_000_000_000:.2f} B"
    else:
        pop_display = "N/A"

    st.metric(
        "👥 Population",
        pop_display
    )

# -----------------------------------------------------
# ROW 1
# -----------------------------------------------------

left,right = st.columns(2)

# =====================================================
# GLOBAL TREND
# =====================================================

with left:

    st.subheader("📈 Global Coffee Consumption Trend")

    trend = (
        df[
            df["Attribute_Description"]=="Domestic Consumption"
        ]
        .groupby("Market_Year",as_index=False)["Value"]
        .sum()
        .sort_values("Market_Year")
    )

    fig = px.line(
        trend,
        x="Market_Year",
        y="Value",
        markers=True,
        color_discrete_sequence=["#8B4513"]
    )

    fig.update_layout(
        height=450,
        xaxis_title="Market Year",
        yaxis_title="Consumption (1000 Bags)",
        template="plotly_white"
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# TOP CONSUMERS
# =====================================================

with right:

    st.subheader("🏆 Top 10 Coffee Consumers")

    top10 = (
        filtered_df[
            filtered_df["Attribute_Description"]=="Domestic Consumption"
        ]
        .groupby("Country_Name",as_index=False)["Value"]
        .sum()
        .sort_values("Value",ascending=False)
        .head(10)
    )

    fig = px.bar(
        top10,
        x="Value",
        y="Country_Name",
        orientation="h",
        text="Value",
        color="Value",
        color_continuous_scale="YlOrBr"
    )

    fig.update_layout(
        height=450,
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Consumption (1000 Bags)",
        yaxis_title="",
        template="plotly_white"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------------------------------
# ROW 2
# -----------------------------------------------------

left,right = st.columns(2)

# =====================================================
# TOP PRODUCERS
# =====================================================

with left:

    st.subheader("🌱 Top Coffee Producers")

    producer = (
        filtered_df[
            filtered_df["Attribute_Description"]=="Production"
        ]
        .groupby("Country_Name",as_index=False)["Value"]
        .sum()
        .sort_values("Value",ascending=False)
        .head(10)
    )

    fig = px.bar(
        producer,
        x="Country_Name",
        y="Value",
        color="Value",
        text="Value",
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Country",
        yaxis_title="Production (1000 Bags)",
        template="plotly_white"
    )

    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# ATTRIBUTE DISTRIBUTION
# =====================================================

with right:

    st.subheader("🥧 Coffee Market Activity")

    activity = (
        filtered_df
        .groupby("Attribute_Description", as_index=False)["Value"]
        .sum()
        .sort_values("Value", ascending=False)
    )

    fig = px.pie(
        activity,
        values="Value",
        names="Attribute_Description",
        hole=0.55,
        color_discrete_sequence=px.colors.sequential.YlOrBr
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# WORLD MAP
# -----------------------------------------------------

st.markdown("---")

st.subheader("🌍 Global Coffee Consumption Map")

map_df = (
    df[
        df["Attribute_Description"] == "Domestic Consumption"
    ]
    .groupby(
        ["Country_Name", "ISO3 CODE"],
        as_index=False
    )
    .agg(
        {
            "Value":"sum",
            "Population":"max"
        }
    )
)

fig = px.choropleth(
    map_df,
    locations="ISO3 CODE",
    color="Value",
    hover_name="Country_Name",
    hover_data={
        "Population":":,.0f",
        "Value":":,.0f"
    },
    color_continuous_scale="YlOrBr",
    projection="natural earth"
)

fig.update_layout(
    height=650,
    template="plotly_white",
    margin=dict(l=0,r=0,t=20,b=0)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------------------------
# BUSINESS INSIGHTS
# -----------------------------------------------------

st.markdown("---")

st.subheader("💡 Executive Summary")

consumer = (
    filtered_df[
        filtered_df["Attribute_Description"]=="Domestic Consumption"
    ]
    .groupby("Country_Name")["Value"]
    .sum()
    .sort_values(ascending=False)
)

producer = (
    filtered_df[
        filtered_df["Attribute_Description"]=="Production"
    ]
    .groupby("Country_Name")["Value"]
    .sum()
    .sort_values(ascending=False)
)

top_consumer = consumer.index[0]
top_producer = producer.index[0]

latest_consumption = consumer.iloc[0]
latest_production = producer.iloc[0]

left,right = st.columns(2)

with left:

    st.success(f"""

### 📌 Key Findings

✔ Highest Coffee Consumer

**{top_consumer}**

**{latest_consumption:,.0f} Thousand Bags**

---

✔ Highest Coffee Producer

**{top_producer}**

**{latest_production:,.0f} Thousand Bags**

---

✔ Countries Covered

**{countries}**

""")

with right:

    st.info("""

### 🚀 ACME Recommendation

Recommended Markets

🥇 Brazil

🥈 United States

🥉 Japan

Reason

• Strong domestic demand

• Large customer base

• Mature coffee ecosystem

• Long-term market opportunity

""")

# -----------------------------------------------------
# DOWNLOAD BUTTON
# -----------------------------------------------------

st.markdown("---")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Filtered Dataset",

    data=csv,

    file_name=f"coffee_market_{selected_year}.csv",

    mime="text/csv"

)

# -----------------------------------------------------
# RAW DATA
# -----------------------------------------------------

with st.expander("📄 View Raw Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# -----------------------------------------------------
# DATA QUALITY
# -----------------------------------------------------

st.markdown("---")

st.subheader("📊 Dataset Information")

c1,c2,c3 = st.columns(3)

with c1:

    st.metric(
        "Rows",
        f"{len(filtered_df):,}"
    )

with c2:

    st.metric(
        "Columns",
        len(filtered_df.columns)
    )

with c3:

    st.metric(
        "Market Year",
        selected_year
    )

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>

### ☕ Coffee Market Analytics Dashboard

Developed by **Akash Dubey**

Python • Pandas • PostgreSQL • SQL • Plotly • Streamlit

Global Coffee Market Analysis Project

</div>
""",
unsafe_allow_html=True
)