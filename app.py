import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Uber Demand AI | Analytics",
    page_icon="🚗",
    layout="wide"
)

# --- UBER MODERN DARK CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #000000;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #060606;
        border-right: 1px solid #262626;
    }

    /* Professional Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #111111;
        border: 1px solid #262626;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    /* Typography */
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
        letter-spacing: -0.5px;
    }
    
    /* Blue Accents for Metrics */
    label[data-testid="stMetricLabel"] {
        color: #276EF1 !important; /* Uber Blue */
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.8rem !important;
    }

    /* Tab Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #111111;
        border: 1px solid #262626;
        border-radius: 4px;
        padding: 8px 20px;
        color: #EEEEEE;
    }
    .stTabs [aria-selected="true"] {
        background-color: #276EF1 !important;
        border: 1px solid #276EF1 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING (Safely) ---
@st.cache_data
def load_data():
    try:
        hour_df = pd.read_csv("data/cleaned_data/rides_by_hour.csv")
        weekday_df = pd.read_csv("data/cleaned_data/rides_by_weekday.csv")
        base_df = pd.read_csv("data/cleaned_data/rides_by_base.csv")
        location_df = pd.read_csv("data/cleaned_data/location_demand.csv")
        full_df = pd.read_csv("data/cleaned_data/uber_cleaned.csv")
        return hour_df, weekday_df, base_df, location_df, full_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None, None, None

hour_df, weekday_df, base_df, location_df, full_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png", width=120)
    st.markdown("### Operational Intelligence")
    st.divider()
    st.info("⚡ **Live Demand Monitoring**")
    st.markdown("This dashboard tracks geospatial ride density and temporal peaks to optimize fleet distribution.")
    st.divider()
    if st.button("Refresh Fleet Data"):
        st.cache_data.clear()
        st.rerun()

# --- HEADER ---
st.title("Uber Ride Demand Analytics")
st.markdown("<p style='color:#A6A6A6; font-size:1.2rem;'>Real-time Geospatial Insights & Operational Performance</p>", unsafe_allow_html=True)

# --- KPI SECTION ---
if full_df is not None:
    total_rides = len(full_df)
    peak_hour = hour_df.iloc[hour_df.iloc[:,1].idxmax()][0]
    peak_weekday = weekday_df.iloc[weekday_df.iloc[:,1].idxmax()][0]
    top_base = base_df.iloc[base_df.iloc[:,1].idxmax()][0]

    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Rides", f"{total_rides:,}")
    c2.metric("Peak Hour", f"{peak_hour}:00")
    c3.metric("Peak Weekday", peak_weekday)
    c4.metric("Top Base", top_base)

st.write("")
st.divider()

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Temporal Trends", "📍 Geospatial Demand", "📂 Explorer"])

with tab1:
    col_l, col_r = st.columns(2)
    
    with col_l:
        fig1 = px.line(hour_df, x=hour_df.columns[0], y=hour_df.columns[1],
                       title="Demand Surge by Hour", template="plotly_dark",
                       color_discrete_sequence=['#276EF1'])
        fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)

    with col_r:
        fig2 = px.bar(weekday_df, x=weekday_df.columns[0], y=weekday_df.columns[1],
                      title="Weekly Demand Distribution", template="plotly_dark",
                      color_discrete_sequence=['#06C167']) # Uber Green for success
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.bar(base_df, x=base_df.columns[0], y=base_df.columns[1],
                  title="Ride Volume by Uber Base", template="plotly_dark",
                  color=base_df.columns[1], color_continuous_scale='Blues')
    fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("High-Density Pickup Zones")
    fig4 = px.scatter_mapbox(location_df,
                            lat="Lat", lon="Lon",
                            size=location_df.columns[-1],
                            color=location_df.columns[-1],
                            color_continuous_scale="Viridis",
                            size_max=15, zoom=10,
                            mapbox_style="carto-darkmatter",
                            title="Heatmap of Pickup Requests")
    fig4.update_layout(margin={"r":0,"t":40,"l":0,"b":0}, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("---")
    st.header("Business Intelligence (Power BI) Dashboard")
    st.image("assets/dashboard.png", use_container_width=True, caption="Enterprise Power BI Deep-Dive")

with tab3:
    st.subheader("Raw Data Inspection")
    if full_df is not None:
        st.dataframe(full_df.head(1000), use_container_width=True)
        st.download_button("Export Data", full_df.to_csv(), "uber_export.csv", "text/csv")

# --- FOOTER ---
st.markdown("<br><hr><center style='color:#666666;'>Uber Demand Analytics | Ops Intelligence Unit © 2026</center>", unsafe_allow_html=True)