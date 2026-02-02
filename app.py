import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ Page Config ------------------
st.set_page_config(page_title="🥑 Avocado EDA Dashboard", layout="wide")

# ------------------ Title ------------------
st.title("🥑 Avocado Price Analysis Dashboard")
st.markdown("Exploratory Data Analysis (EDA) on Avocado Dataset")

# ------------------ Load Data ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("avocado.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# ------------------ Sidebar ------------------
st.sidebar.header("🔎 Filters")

region = st.sidebar.selectbox(
    "Select Region",
    options=sorted(df['region'].unique())
)

type_avocado = st.sidebar.radio(
    "Select Type",
    options=df['type'].unique()
)

# ------------------ Filtered Data ------------------
filtered_df = df[(df['region'] == region) & (df['type'] == type_avocado)]

# ------------------ KPI Metrics ------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average Price", f"${filtered_df['AveragePrice'].mean():.2f}")
col2.metric("Total Volume", f"{filtered_df['Total Volume'].sum():,.0f}")
col3.metric("Total Records", filtered_df.shape[0])

# ------------------ Data Preview ------------------
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df.head(20))

# ------------------ Price Trend ------------------
st.subheader("📈 Average Price Trend")

fig, ax = plt.subplots()
ax.plot(filtered_df['Date'], filtered_df['AveragePrice'])
ax.set_xlabel("Date")
ax.set_ylabel("Average Price")
ax.set_title(f"Price Trend in {region} ({type_avocado})")

st.pyplot(fig)

# ------------------ Volume Analysis ------------------
st.subheader("📦 Total Volume Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(filtered_df['Total Volume'], bins=30)
ax2.set_xlabel("Total Volume")
ax2.set_ylabel("Frequency")

st.pyplot(fig2)

# ------------------ Correlation ------------------
st.subheader("🔗 Correlation Analysis")

corr = filtered_df[[
    'AveragePrice',
    'Total Volume',
    '4046', '4225', '4770'
]].corr()

st.dataframe(corr)


