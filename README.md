# Uber Ride Demand Intelligence Platform

An end-to-end data analytics platform that analyzes Uber ride demand patterns in New York City using Python, SQL, Power BI, and Streamlit.

This project processes over 564,000 ride records to generate actionable insights on temporal and geographic demand, enabling better driver allocation and operational efficiency.

---

## Live Demo

Deployed Streamlit Application:  
https://uber-ride-demand-analytics-dashboard-ltj84nqhni8o7dvwdachyg.streamlit.app/

---

## Problem Statement

Ride-sharing platforms generate large volumes of real-time data. However, without proper analysis, this data cannot be leveraged to:

- Identify peak demand hours  
- Detect high-demand locations  
- Optimize driver distribution  
- Reduce passenger wait times  

This project solves these challenges by building a complete analytics pipeline from raw data to interactive insights.

---

## Key Features

- End-to-end data pipeline from raw data to dashboard  
- Time-based demand analysis (hour, day, month)  
- Geographic ride density analysis  
- SQL-based aggregation for scalable analytics  
- Interactive web dashboard using Streamlit  
- Business intelligence dashboard using Power BI  

---

## Dataset

Source: Kaggle – Uber Pickup Data (NYC)

- 564,000+ ride records  
- Features: datetime, latitude, longitude, base code  
- Each row represents a single Uber pickup  

---

## System Architecture

```

Raw Data (CSV)
↓
Data Cleaning & Preprocessing (Pandas)
↓
Feature Engineering
↓
Exploratory Data Analysis
↓
SQL Aggregation Layer
↓
Analytics Data Tables
↓
Power BI Dashboard
↓
Streamlit Interactive App

```

---

## Data Engineering

Data preprocessing and feature engineering were implemented using Pandas.

Key transformations:

- Extracted hour, weekday, and month from timestamps  
- Cleaned missing and inconsistent values  
- Structured datasets for analytics queries  

Output stored in:

```

data/cleaned_data/

```

---

## Exploratory Data Analysis

EDA was performed to identify demand patterns and trends.

Key insights derived:

- Hourly demand distribution  
- Weekday vs weekend comparison  
- Monthly ride trends  
- High-density pickup zones  

Tools used: Matplotlib, Seaborn  

---

## SQL Analytics Layer

SQL queries were used to generate aggregated metrics:

- Rides per hour  
- Rides per weekday  
- Daily ride volume  
- Demand by Uber base  

These queries simulate real-world analytics workflows used in data teams.

---

## Dashboard (Power BI)

The Power BI dashboard provides business-level insights:

- Total rides and peak demand metrics  
- Hourly and weekday trends  
- Geographic distribution  
- Base-level performance  

---

## Interactive Web Application

A Streamlit-based analytics application provides real-time exploration of data.

Features:

- Interactive visualizations (Plotly)  
- Dynamic filtering  
- Clean and responsive UI  
- Fast analytics rendering  

Run locally:

```

streamlit run app.py

````

---

## Key Insights

- Peak demand occurs between 5 PM – 7 PM  
- Weekday demand exceeds weekend demand  
- Manhattan has the highest pickup density  
- Demand spikes are time-dependent and predictable  

---

## Technology Stack

| Category            | Tools            |
|--------------------|------------------|
| Programming        | Python           |
| Data Processing    | Pandas           |
| Visualization      | Plotly           |
| BI Dashboard       | Power BI         |
| Web Framework      | Streamlit        |
| Query Language     | SQL              |
| Analysis           | Jupyter Notebook |
| Version Control    | Git              |

---

## Performance & Scalability

- Efficient handling of 500K+ records  
- SQL-based aggregation reduces computation overhead  
- Modular pipeline design for easy scaling  
- Separation of processing and visualization layers  

---

## Future Enhancements

- Time series forecasting using ML models  
- Real-time streaming analytics  
- Advanced geospatial clustering  
- Driver supply vs demand optimization  

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/CodingWithDevraj/Uber-Ride-Demand-Analytics-Dashboard.git
cd Uber-Ride-Demand-Analytics-Dashboard
````

### 2. Setup Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```
uber-ride-demand-analytics/
│
├── app.py
├── data/
├── notebook/
├── sql/
├── dashboard/
└── README.md
```

---

## Skills Demonstrated

* Data Engineering
* Exploratory Data Analysis
* SQL Analytics
* Dashboard Development
* Data Visualization
* Problem Solving

---

## Author

Devraj Choudhary
B.Tech – Computer Science & Engineering
Gurukul Kangri University

GitHub: [https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)
LinkedIn: [https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)
