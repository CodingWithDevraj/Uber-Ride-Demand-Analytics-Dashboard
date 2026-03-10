---

# 🚕 Uber Ride Demand Intelligence Platform

---

# 🚕 Uber Ride Demand Intelligence Platform

![Python](https://img.shields.io/badge/Python-Analytics-blue)
![SQL](https://img.shields.io/badge/SQL-Data%20Querying-orange)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20App-red)

An **end-to-end ride demand analytics platform** that analyzes **Uber pickup patterns in New York City** using **Python, SQL, Power BI, and Streamlit**.

The project processes **564,000+ Uber pickup records** to uncover demand patterns across **time, geography, and operational bases**, and delivers insights through both:

• **Interactive Streamlit analytics application**
• **Business intelligence dashboard in Power BI**

The goal is to help ride-sharing platforms **optimize driver allocation, identify peak demand periods, and improve operational efficiency**.

---

# 🚀 Project Overview

Ride-sharing services generate massive volumes of operational data every day. Extracting insights from this data enables companies to:

• Predict peak ride demand periods
• Identify high-demand geographic zones
• Optimize driver deployment
• Improve service efficiency

This project builds a **complete analytics pipeline** that transforms raw Uber pickup data into **actionable business intelligence**.

The system performs:

1. Data cleaning and preprocessing
2. Exploratory data analysis
3. SQL-based demand aggregation
4. Dashboard visualization
5. Interactive analytics application

---

# 📊 Dataset

Dataset Source: **Kaggle – Uber Pickup Data (NYC)**

Dataset contains:

• **564,000+ Uber ride records**
• Pickup datetime
• Latitude
• Longitude
• Uber base code

Each record represents a **single Uber pickup event in New York City**.

---

# ⚙️ Data Pipeline

The project follows a structured **analytics workflow used in industry data teams**.

```
Raw Dataset
   ↓
Data Cleaning (Python / Pandas)
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
SQL Data Aggregation
   ↓
Prepared Analytics Tables
   ↓
Power BI Dashboard
   ↓
Streamlit Interactive Analytics App
```

---

# 🧹 Data Cleaning & Feature Engineering

Data preprocessing was performed using **Python (Pandas)**.

Key transformations include extracting temporal features from pickup timestamps:

• Hour of ride
• Day of month
• Weekday
• Month

These features allow detailed **time-based ride demand analysis**.

Cleaned datasets are stored in:

```
data/cleaned_data/
```

---

# 🔎 Exploratory Data Analysis

EDA was conducted using **Matplotlib and Seaborn** to identify ride demand patterns.

Key analyses include:

• Hourly ride demand distribution
• Weekday demand comparison
• Monthly ride trends
• Pickup location density

Notebooks used:

```
notebook/eda_analysis.ipynb
```

---

# 🗄 SQL Demand Aggregation

SQL queries were used to calculate important demand metrics.

Examples include:

• Total rides per hour
• Total rides per weekday
• Ride demand by Uber base
• Daily ride volume

SQL queries are stored in:

```
sql/analysis_queries.sql
```

These aggregated datasets are exported for dashboard visualization.

---

# 📊 Power BI Dashboard

A **business intelligence dashboard** was developed using Power BI.

Dashboard features include:

### KPI Metrics

• Total rides
• Peak demand hour
• Most active weekday

### Visualizations

• Hourly demand trends
• Weekday ride distribution
• Monthly ride activity
• Uber base performance
• Geographic pickup distribution

Dashboard file:

```
dashboard/UBER_VISUALS.pbix
```

---

# 🖥 Streamlit Analytics Application

A modern **interactive analytics app** was developed using **Streamlit and Plotly**.

The application includes:

• Interactive ride demand visualizations
• Dynamic filtering of demand metrics
• Dark-themed professional UI
• Interactive charts using Plotly

Main application file:

```
app.py
```

Run locally with:

```
streamlit run app.py
```

---

# 📁 Project Structure

```
uber-ride-demand-analytics
│
├── app.py
│
├── assets
│   └── dashboard.png
│
├── dashboard
│   └── UBER_VISUALS.pbix
│
├── data
│   ├── raw
│   │   └── uber-raw-data-apr14.csv
│   │
│   ├── cleaned_data
│   │   ├── location_clusters.csv
│   │   ├── location_demand.csv
│   │   ├── rides_by_base.csv
│   │   ├── rides_by_day.csv
│   │   └── rides_by_hour.csv
│   │
│   └── powerbi_data
│       ├── pickup_locations.csv
│       ├── rides_by_base.csv
│       ├── rides_by_day.csv
│       ├── rides_by_hour.csv
│       └── rides_by_weekday.csv
│
├── notebook
│   ├── data_cleaning.ipynb
│   └── eda_analysis.ipynb
│
├── sql
│   └── analysis_queries.sql
│
└── README.md
```

---

# 📈 Key Insights

Analysis of the dataset reveals several important demand patterns:

• Ride demand peaks between **5 PM – 7 PM**, reflecting evening commute traffic
• **Weekday demand is higher than weekend demand**
• Certain days show **spikes in ride activity**
• **Manhattan has the highest pickup density**

These insights help ride-sharing companies **optimize driver allocation and reduce passenger wait times**.

<img width="2767" height="1600" alt="dashboard" src="https://github.com/user-attachments/assets/cd269dd4-6ab7-4c46-b9ee-0402cd282fbb" />




---

# 🛠 Technology Stack

| Category          | Tools            |
| ----------------- | ---------------- |
| Programming       | Python           |
| Data Processing   | Pandas           |
| Visualization     | Plotly           |
| Dashboard         | Power BI         |
| Web App           | Streamlit        |
| Database Querying | SQL              |
| Analysis          | Jupyter Notebook |
| Version Control   | GitHub           |

---

# 💡 Skills Demonstrated

This project showcases several **industry-relevant data analytics skills**:

• Data Cleaning & Feature Engineering
• Exploratory Data Analysis
• SQL Data Aggregation
• Business Intelligence Dashboard Development
• Interactive Data Applications
• Analytical Storytelling

---

# 🔮 Future Improvements

Possible enhancements include:

• Time series **ride demand forecasting**
• Real-time ride demand analytics
• Advanced geospatial clustering
• Driver supply vs demand optimization

---

# 👨‍💻 Author

**Devraj Choudhary**

B.Tech – Computer Science & Engineering
Gurukul Kangri Deemed to be University

Interests

• Data Analytics
• Machine Learning
• Business Intelligence

GitHub
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

LinkedIn
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)

---




