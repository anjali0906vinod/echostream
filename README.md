EchoStream — End-to-End Spotify Music Data Engineering Pipeline
Python • Azure SQL Database • Power BI • Data Engineering

📌 Overview

EchoStream is an end-to-end data engineering & analytics project built on Spotify music data, designed to simulate a real industry-level data pipeline.

The project takes raw Spotify track & artist data, processes it through an ETL workflow in Python, loads it into Azure SQL Database, and visualizes insights through an interactive Power BI dashboard.

This project is currently under development, with components being added in phases.

🎯 Objectives

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
