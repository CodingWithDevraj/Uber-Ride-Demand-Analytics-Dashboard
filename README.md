# Uber Ride Demand Intelligence Platform

An **end-to-end ride demand analytics platform** that analyzes **Uber pickup patterns in New York City** using **Python, SQL, Power BI, and Streamlit**.

The project processes **564,000+ Uber pickup records** to uncover demand patterns across **time, geography, and operational bases**, and delivers insights through both:

• Interactive Streamlit analytics application
• Business intelligence dashboard in Power BI

The goal is to help ride-sharing platforms **optimize driver allocation, identify peak demand periods, and improve operational efficiency**.

---

# Live Demo

The project is deployed as an interactive web application using Streamlit:

**Live Application:**
[https://uber-ride-demand-analytics-dashboard-ltj84nqhni8o7dvwdachyg.streamlit.app/](https://uber-ride-demand-analytics-dashboard-ltj84nqhni8o7dvwdachyg.streamlit.app/)

This allows users to explore ride demand analytics in real-time without setting up the project locally.

---

# Project Overview

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

# Dataset

Dataset Source: **Kaggle – Uber Pickup Data (NYC)**

Dataset contains:

• 564,000+ Uber ride records
• Pickup datetime
• Latitude
• Longitude
• Uber base code

Each record represents a **single Uber pickup event in New York City**.

---

# Data Pipeline

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

# Data Cleaning & Feature Engineering

Data preprocessing was performed using **Python (Pandas)**.

Key transformations include:

• Hour of ride
• Day of month
• Weekday
• Month

Cleaned datasets are stored in:

```
data/cleaned_data/
```

---

# Exploratory Data Analysis

EDA was conducted using **Matplotlib and Seaborn**.

Key analyses:

• Hourly ride demand distribution
• Weekday demand comparison
• Monthly ride trends
• Pickup location density

---

# SQL Demand Aggregation

Examples:

• Total rides per hour
• Total rides per weekday
• Ride demand by Uber base
• Daily ride volume

---

# Power BI Dashboard

Includes:

• KPI metrics (total rides, peak hour, weekday trends)
• Demand visualizations
• Geographic analysis

---

# Streamlit Analytics Application

Features:

• Interactive charts (Plotly)
• Dynamic filters
• Professional UI

Run locally:

```
streamlit run app.py
```

---

# Project Structure

```
uber-ride-demand-analytics
├── app.py
├── dashboard/
├── data/
├── notebook/
├── sql/
└── README.md
```

---

# Key Insights

• Peak demand: 5 PM – 7 PM
• Weekdays > Weekends
• Manhattan highest demand
• Demand spikes on specific days

---

# Technology Stack

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

# Skills Demonstrated

• Data Cleaning & Feature Engineering
• Exploratory Data Analysis
• SQL Aggregation
• Dashboard Development
• Interactive Applications

---

# How to Run This Project

```bash
git clone https://github.com/CodingWithDevraj/Uber-Ride-Demand-Analytics-Dashboard.git
cd Uber-Ride-Demand-Analytics-Dashboard

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

# Future Improvements

• Demand forecasting
• Real-time analytics
• Advanced geospatial clustering
• Supply-demand optimization

---

# Author

**Devraj Choudhary**
B.Tech – Computer Science & Engineering
Gurukul Kangri Deemed to be University

GitHub
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

LinkedIn
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)
