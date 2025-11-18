EchoStream — End-to-End Spotify Music Data Engineering Pipeline
Python • Azure SQL Database • Power BI • Data Engineering

 OVERVIEW 

EchoStream is an end-to-end data engineering & analytics project built on Spotify music data, designed to simulate a real industry-level data pipeline.

The project takes raw Spotify track & artist data, processes it through an ETL workflow in Python, loads it into Azure SQL Database, and visualizes insights through an interactive Power BI dashboard.

This project is currently under development, with components being added in phases.

OBJECTIVES 

Build a working ETL pipeline with Python

Clean, transform, and structure Spotify data

Create & manage a cloud database with Azure SQL

Design normalized tables for analytics

Write SQL queries to explore trends

Build a Power BI dashboard connected directly to Azure SQL

Document the entire pipeline in a clear, industry-style structure 

ARCHITECTURE 
```
           ┌────────────────────┐
           │  Spotify Dataset   │
           └─────────┬──────────┘
                     │
              (Ingestion - Python)
                     │
           ┌─────────▼─────────┐
           │   Data Cleaning    │
           │   & Transformation │
           └─────────┬─────────┘
                     │
            (Load to Azure SQL)
                     │
           ┌─────────▼─────────┐
           │  Azure SQL DB      │
           │ (Fact & Dimension) │
           └─────────┬─────────┘
                     │
           (Connect from Power BI)
                     │
           ┌─────────▼─────────┐
           │   Power BI Report  │
           └────────────────────┘
```
PROJECT OVERVIEW 
1. Layer	Tech Used	Purpose
2. Ingestion	Python, APIs / CSVs	Collect raw music streaming data
3. Processing	Pandas, NumPy	Clean + transform data into usable tables
4. Storage	Azure SQL Database	Store facts & dimensions for querying
5. Analytics	SQL queries	Generate insights on streams, artists, genres
6. Dashboard	Power BI	Build a clean, interactive dashboard
7. Orchestration (Future)	Airflow	Automate the entire pipeline

Key Features (Planned)

✔ Data ingestion pipeline for music metadata and streaming logs

✔ Data cleaning and transformation using Pandas

✔ Star schema design (fact + dimension tables)

✔ Load final tables into Azure SQL

✔ Complex SQL queries for analytics

✔ Power BI dashboard for metrics like:

Top artists

Most streamed genres

Listener habits & trends

Daily/Monthly stream patterns

End-to-end automation with Airflow 


 PROJECT STRUCTURE 
 
```
EchoStream/
│
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── load/
│   └── utils/
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│
├── dashboards/
│   └── PowerBI/
│
├── data/
│   ├── raw/
│   └── processed/
│
└── README.md
```
TECH STACK : 

1. Python (Pandas, NumPy, Requests)
2. Azure SQL Database
3. Power BI
4. SQL (Joins, Window Functions, CTEs, Aggregations)
5. Git & GitHub
6. Airflow 

CURRENT STATUS 

🔹 Project setup in progress
🔹 README initialized
🔹 Data schema + pipeline design next

📬 Contact
Anjali Vinod
BCA 3rd Year — Data Science
Email: anjali2006vinod@gmail.com