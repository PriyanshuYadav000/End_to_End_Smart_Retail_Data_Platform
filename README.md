# End-to-End Smart Retail Analytics Platform

## Project Overview

Built an end-to-end cloud-based Retail Analytics Platform that ingests retail data from REST APIs, processes and transforms data through ETL pipelines, stores data in a scalable data warehouse, and generates actionable business insights through interactive Power BI dashboards.

The project demonstrates modern Data Engineering, Business Intelligence, and Analytics workflows using Microsoft Azure services and industry-standard data practices.

---

## Architecture

```text
DummyJSON API
        ↓
Azure Data Lake Storage Gen2 (Raw Layer)
        ↓
Azure Data Factory
        ↓
Data Flow Transformation
        ↓
Azure Data Lake Storage Gen2 (Enriched Layer)
        ↓
Azure SQL Database
        ↓
Power BI Dashboard
        ↓
AI Insight Engine (In Progress)
```

![Architecture](screenshots/architecture.png)

---

## Dataset Statistics

| Dataset    | Records |
| ---------- | ------: |
| Products   |     194 |
| Users      |     200 |
| Carts      |     200 |
| Categories |      24 |

---

## Technology Stack

### Data Engineering

* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure SQL Database
* ETL Pipelines
* Data Warehousing

### Analytics & BI

* Power BI
* DAX
* Excel
* Power Query

### Programming

* Python
* SQL
* Pandas
* NumPy

### Cloud

* Microsoft Azure
* REST APIs

---

## Key Features

* Automated API Data Ingestion
* End-to-End ETL Pipeline Development
* Data Cleaning and Transformation
* Cloud Data Lake Architecture
* Data Warehouse Design
* Data Validation and Quality Checks
* Interactive Power BI Dashboards
* KPI Monitoring and Business Reporting
* Revenue and Customer Analytics
* Scalable Analytics Architecture

---

## Data Warehouse Design

Implemented a dimensional data model using:

### Fact Tables

* fact_carts

### Dimension Tables

* dim_products
* dim_users

The warehouse design supports efficient analytical queries and business reporting.

---

## Azure Data Factory Pipeline

Automated data ingestion, transformation, and loading using Azure Data Factory pipelines.

![ADF Pipeline](screenshots/adf_pipeline.png)

---

## Data Transformation Flow

Implemented transformation logic for cleansing, enrichment, validation, and business rule application.

![Data Flow](screenshots/data_flow.png)

---

## Azure SQL Data Warehouse

Loaded curated datasets into Azure SQL Database for reporting and analytics.

![Azure SQL Tables](screenshots/azure_sql_tables.png)

---

## Power BI Dashboard

Developed interactive dashboards to monitor:

* Revenue Trends
* Product Performance
* Category Analysis
* Customer Insights
* Business KPIs

### Dashboard Overview

![Power BI Dashboard](screenshots/powerbi_dashboard_overview.png)

### Revenue Analysis

![Revenue Analysis](screenshots/revenue_analysis.png)

### Product Category Analysis

![Products by Category](screenshots/products_by_category.png)

### Top Products Analysis

![Top Products](screenshots/top_10_products.png)

### User Demographics

![User Demographics](screenshots/user_demographics.png)

---

## Business Insights Generated

* Identified top-performing product categories.
* Analyzed revenue contribution across product segments.
* Evaluated customer demographics and purchasing behavior.
* Monitored operational KPIs through interactive dashboards.
* Improved reporting accuracy through automated validation workflows.

---

## Future Enhancements

* AI-Powered Insight Engine
* Natural Language Querying
* Predictive Analytics and Forecasting
* Azure Databricks Integration
* PySpark-Based Data Processing
* Real-Time Data Streaming

---

## Repository Structure

```text
End_to_End_Smart_Retail_Analytics_Platform

data/
├── raw/
├── processed/

pipelines/
├── adf/

sql/
├── validation_queries.sql
├── business_analytics.sql

screenshots/

README.md
```

---

## Author

**Priyanshu Yadav**

Aspiring Data Analyst | Data Engineer 
