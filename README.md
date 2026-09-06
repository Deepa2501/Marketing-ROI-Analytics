````markdown
# 📊 Marketing ROI Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![DAX](https://img.shields.io/badge/DAX-KPI%20Analysis-purple)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green)

> An end-to-end **Marketing Analytics & Business Intelligence** project that transforms **55,000+ marketing campaign records** into actionable business insights using **Python, PostgreSQL, SQL, Statistical Analysis, Machine Learning, Power BI, and DAX**.

---

## 🎯 Project Overview

Marketing teams often need to understand which campaigns, channels, and customer segments generate the highest returns.

This project develops a complete **Marketing ROI Analytics and Business Intelligence solution** covering the full analytics lifecycle:

**Raw Data → Data Cleaning → ETL → PostgreSQL → SQL Analysis → Statistical Analysis → A/B Testing → Machine Learning → Power BI → DAX → Business Insights**

### Business Objectives

- Analyze campaign performance and ROI
- Measure marketing channel effectiveness
- Track revenue, clicks, leads, and conversions
- Identify high-performing customer segments
- Evaluate marketing funnel performance
- Compare campaign performance using A/B testing
- Analyze marketing spend efficiency
- Build predictive ROI models
- Create executive-level business dashboards
- Support data-driven marketing decisions

---

## 📊 Dataset

The project uses a marketing campaign performance dataset containing **55,000+ records**.

### Dataset Features

| Column | Description |
|---|---|
| Campaign_ID | Unique campaign identifier |
| Campaign_Type | Type of marketing campaign |
| Target_Audience | Target customer audience |
| Duration | Campaign duration |
| Channel_Used | Marketing channel |
| Impressions | Number of campaign impressions |
| Clicks | Number of clicks |
| Leads | Number of generated leads |
| Conversions | Number of conversions |
| Revenue | Revenue generated |
| Acquisition_Cost | Cost of acquiring customers |
| ROI | Return on Investment |
| Language | Campaign language |
| Engagement_Score | Customer engagement score |
| Customer_Segment | Customer segment |
| Date | Campaign date |

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database | PostgreSQL |
| SQL | PostgreSQL SQL |
| Visualization | Power BI, DAX, Matplotlib, Plotly |
| Statistical Analysis | Statistical Analysis, A/B Testing |
| Machine Learning | Scikit-learn |
| ETL | Python |
| Version Control | Git, GitHub |
| Source Data | Excel (.xlsx) |

---

# 🔄 Complete Project Workflow

```text
                    ┌─────────────────────────┐
                    │   Raw Marketing Data    │
                    │       Excel Dataset     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Data Cleaning        │
                    │     Python + Pandas     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Feature Engineering    │
                    │    Derived Metrics      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Python ETL         │
                    │ Validation & Loading     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   PostgreSQL Database   │
                    │   Relational Storage    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      SQL Analysis       │
                    │ KPI & Business Queries  │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┴─────────────────┐
                ▼                                  ▼
      ┌─────────────────────┐            ┌─────────────────────┐
      │ Statistical Analysis│            │ Machine Learning    │
      │ & A/B Testing       │            │ ROI Prediction      │
      └──────────┬──────────┘            └──────────┬──────────┘
                 │                                  │
                 └────────────────┬─────────────────┘
                                  ▼
                    ┌─────────────────────────┐
                    │      Power BI           │
                    │    DAX + Dashboards     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Key Business Insights  │
                    │   Data-Driven Decisions │
                    └─────────────────────────┘
````

---

# 🧹 Data Cleaning & ETL

The project begins by validating and transforming raw marketing campaign data into a clean, structured, analysis-ready dataset.

### Data Cleaning Activities

* Data validation
* Duplicate checks
* Data type validation
* Missing value handling
* Column standardization
* Data transformation
* Feature preparation
* Data quality checks

### ETL Flow

```text
Raw Excel Data
      ↓
Validation
      ↓
Cleaning
      ↓
Transformation
      ↓
Feature Engineering
      ↓
Validation
      ↓
PostgreSQL Loading
```

---

# 🐍 Python Pipeline

Python is used throughout the project for data preparation, exploratory analysis, statistical testing, and predictive modeling.

### Python Scripts

```text
python/
│
├── etl.py
├── cleaning.py
├── eda.py
├── statistical_analysis.py
├── ab_testing.py
├── roi_prediction.py
├── early_roi_prediction.py
├── cost_only_model.py
├── strategy_roi_prediction.py
├── roi_leakage_check.py
└── ml_visualization.py
```

### Python Responsibilities

* Data cleaning
* Data transformation
* ETL automation
* Exploratory Data Analysis
* Statistical analysis
* A/B testing
* Feature engineering
* ROI prediction
* Model evaluation
* Visualization

---

# 🗄️ PostgreSQL Database

PostgreSQL is used as the relational database layer for storing and analyzing cleaned marketing campaign data.

### Main Table

```text
marketing_campaigns
```

### Database Workflow

```text
Clean Dataset
      ↓
PostgreSQL Database
      ↓
SQL Queries
      ↓
Aggregations & KPIs
      ↓
Business Analysis
```

### SQL Files

```text
sql/
│
├── schema.sql
├── analysis.sql
├── advanced_analysis.sql
└── kpi_queries.sql
```

---

# 📈 SQL Analysis

The project contains **35+ SQL queries** covering both basic and advanced analytical requirements.

### SQL Concepts Used

* SELECT
* WHERE
* GROUP BY
* HAVING
* ORDER BY
* Aggregate Functions
* CASE Statements
* INNER JOIN
* LEFT JOIN
* Subqueries
* CTEs
* Window Functions
* Ranking Functions
* Date-Based Analysis
* KPI Calculations

### Business Questions Answered

* What is the total revenue generated?
* What is the average ROI?
* Which campaign types perform best?
* Which channels generate the highest revenue?
* Which customer segments contribute the most revenue?
* What are the monthly revenue trends?
* Which campaigns have the highest ROI?
* What is the conversion rate?
* Which marketing channels are most efficient?

---

# 📊 Statistical Analysis & A/B Testing

Statistical analysis is used to evaluate marketing campaign performance and compare different campaign strategies.

### Analysis Includes

* ROI comparison
* Campaign performance comparison
* Channel-level comparison
* Campaign variance analysis
* Statistical testing
* Strategy effectiveness

### A/B Testing Workflow

```text
Campaign Group A
       │
       ▼
Performance Metrics
       │
       ├──────────────┐
       │              │
       ▼              ▼
   Statistical     Campaign
   Comparison      Evaluation
       ▲              ▲
       │              │
       └──────────────┘
       │
Campaign Group B
```

### A/B Testing Script

```bash
python python/ab_testing.py
```

---

# 🤖 Machine Learning Analysis

The project includes exploratory machine learning analysis focused on ROI-related prediction and campaign performance.

### Machine Learning Components

* ROI Prediction
* Early ROI Prediction
* Cost-Based Modeling
* Strategy ROI Prediction
* Feature Importance
* Model Comparison
* Residual Analysis
* Error Analysis
* ROI Leakage Checks
* Prediction Visualization

### Machine Learning Workflow

```text
Marketing Data
      ↓
Feature Engineering
      ↓
Train / Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Feature Importance
      ↓
Prediction Analysis
```

### ML Scripts

```text
roi_prediction.py
early_roi_prediction.py
cost_only_model.py
strategy_roi_prediction.py
roi_leakage_check.py
ml_visualization.py
```

---

# 📊 Power BI Dashboard

The Power BI dashboard converts analytical results into an interactive Business Intelligence solution for executive and marketing performance analysis.

---

# 📄 Dashboard 1 — Executive Overview

The Executive Overview provides a high-level summary of overall marketing performance.

### Key Features

- KPI Cards
- Total Revenue
- Average ROI
- Total Campaigns
- Revenue Trend
- Revenue by Campaign Type
- Revenue by Marketing Channel
- Customer Segment Analysis
- Top Campaigns
- Interactive Filters

### Dashboard Preview
![Executive Overview Dashboard](screenshots/Executive_Overview.png)

---

# 📄 Dashboard 2 — Campaign Performance

The Campaign Performance dashboard focuses on campaign-level and channel-level effectiveness.

### Key Features

- Campaign Performance
- Marketing Channel Analysis
- ROI Comparison
- Target Audience Performance
- Language Analysis
- Engagement Analysis
- Campaign Effectiveness

### Dashboard Preview
![Campaign Performance Dashboard](screenshots/Campaign_performance.png)

---

# 📄 Dashboard 3 — Customer & Marketing Insights

This dashboard provides deeper insights into customer segments and marketing funnel performance.

### Key Features

- Marketing Funnel
- ROI Distribution
- Customer Segment Performance
- Revenue Trend
- Channel Performance Matrix
- Customer Engagement
- Executive Business Insights

### Dashboard Preview
![Customer & Marketing Insights Dashboard](screenshots/Customer_&_Marketing_Insights.png)

# 📌 Key KPIs

The Power BI dashboards track important marketing performance indicators.

| KPI                       | Purpose                              |
| ------------------------- | ------------------------------------ |
| 💰 Total Revenue          | Measures overall campaign revenue    |
| 📈 Average ROI            | Measures marketing return            |
| 🎯 Total Campaigns        | Tracks campaign volume               |
| 👆 CTR                    | Measures click engagement            |
| ✅ Conversion Rate         | Measures conversion efficiency       |
| 💵 CPA                    | Measures customer acquisition cost   |
| 💳 Average Revenue        | Measures average campaign revenue    |
| 📊 Average Engagement     | Measures customer interaction        |
| 👥 Total Customers        | Tracks customer reach                |
| 🔄 Funnel Conversion Rate | Measures marketing funnel efficiency |

---

# 🧮 DAX & KPI Development

Custom DAX measures are used within Power BI to calculate and visualize important business KPIs.

### DAX Analysis Areas

* Revenue calculations
* ROI calculations
* Campaign counts
* CTR
* Conversion Rate
* CPA
* Engagement metrics
* Funnel metrics
* Time-based analysis
* Campaign performance metrics

### Business Measures

```text
Total Revenue
Average ROI
Total Campaigns
CTR
Conversion Rate
CPA
Average Engagement
Funnel Conversion Rate
```

---

# 💡 Key Business Insights

The analysis generated actionable business insights across campaigns, channels, and customer segments.

### 📈 Campaign Performance

* Social Media campaigns generated the highest ROI.
* High-performing marketing channels can be prioritized for future investment.

### 👥 Customer Segments

* Premium customer segments contributed the largest revenue.
* Segment-level analysis helps identify high-value audiences.

### 🔄 Marketing Funnel

* Funnel analysis highlights opportunities for improving conversions.
* Tracking impressions → clicks → leads → conversions helps identify performance gaps.

### 📊 Customer Engagement

* Customer engagement showed a positive relationship with campaign performance.

### 🌍 Channel & Language Analysis

* Channel-level and language-level analysis revealed differences in campaign effectiveness.

---

# 💼 Business Value

This solution helps marketing teams:

✅ Optimize marketing spend
✅ Improve campaign ROI
✅ Identify high-performing channels
✅ Understand customer segments
✅ Monitor campaign performance
✅ Improve conversion efficiency
✅ Track marketing funnel performance
✅ Support data-driven decision making

---

# 📂 Project Structure

```text
Marketing-ROI-Analytics/
│
├── 📁 data/
│   ├── 📁 raw/
│   └── 📁 cleaned/
│
├── 📁 python/
│   ├── etl.py
│   ├── cleaning.py
│   ├── eda.py
│   ├── statistical_analysis.py
│   ├── ab_testing.py
│   ├── roi_prediction.py
│   ├── early_roi_prediction.py
│   ├── cost_only_model.py
│   ├── strategy_roi_prediction.py
│   ├── roi_leakage_check.py
│   └── ml_visualization.py
│
├── 📁 sql/
│   ├── schema.sql
│   ├── analysis.sql
│   ├── advanced_analysis.sql
│   └── kpi_queries.sql
│
├── 📁 powerbi/
│   └── Marketing_ROI_Analytics.pbix
│
├── 📁 screenshots/
│   ├── Executive_Overview.png
│   ├── Campaign_performance.png
│   └── Customer_&_Marketing_Insights.png
│
├── 📁 reports/
│   ├── EDA visualizations
│   ├── ROI analysis results
│   ├── Model comparison results
│   ├── Feature importance results
│   ├── Prediction outputs
│   ├── Residual & error analysis
│   └── A/B testing visualizations
│
├── 📁 docs/
│   └── Data_Dictionary.md
│
├── 📁 dashboard/
├── 📁 excel/
├── 📁 images/
├── 📁 ml/
├── 📁 workflow/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 LICENSE
└── 📄 .gitignore
```

---

# ▶️ How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Deepa2501/Marketing-ROI-Analytics.git
cd Marketing-ROI-Analytics
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Data Cleaning & ETL

```bash
python python/etl.py
```

## 4️⃣ Set Up PostgreSQL

Create the PostgreSQL database and execute:

```text
sql/schema.sql
```

Then run the analysis queries:

```text
sql/analysis.sql
sql/advanced_analysis.sql
sql/kpi_queries.sql
```

## 5️⃣ Run Statistical Analysis

```bash
python python/statistical_analysis.py
```

## 6️⃣ Run A/B Testing

```bash
python python/ab_testing.py
```

## 7️⃣ Run ROI Prediction

```bash
python python/roi_prediction.py
```

## 8️⃣ Open Power BI Dashboard

Open:

```text
powerbi/Marketing_ROI_Analytics.pbix
```

using **Microsoft Power BI Desktop**.

---

# 📸 Dashboard Screenshots

All dashboard previews are available in:

```text
screenshots/
```

### Available Dashboard Pages

1. Executive Overview
2. Campaign Performance
3. Customer & Marketing Insights

---

# 🧠 Skills Demonstrated

### Data Analytics

* Data Cleaning
* Exploratory Data Analysis
* Statistical Analysis
* KPI Development
* Business Analysis

### Python

* Pandas
* NumPy
* ETL Automation
* Data Transformation
* Statistical Analysis
* Machine Learning
* Visualization

### SQL

* Joins
* CTEs
* Aggregations
* Window Functions
* Ranking
* Subqueries
* KPI Queries
* Advanced SQL Analytics

### Business Intelligence

* Power BI
* DAX
* Interactive Dashboards
* KPI Reporting
* Data Storytelling
* Executive Reporting

### Database

* PostgreSQL
* Relational Database
* Data Modeling
* SQL Analytics

### Version Control

* Git
* GitHub

---

# 🌟 Project Highlights

```text
✔ 55,000+ Marketing Campaign Records
✔ Automated Python ETL Pipeline
✔ PostgreSQL Database
✔ 35+ SQL Queries
✔ Statistical Analysis
✔ A/B Testing
✔ ROI Predictive Modeling
✔ Custom DAX Measures
✔ Interactive Power BI Dashboards
✔ Executive-Level Business Insights
```

---

# 🚀 Future Improvements

Potential future enhancements include:

* Real-time marketing data ingestion
* Automated Power BI refresh
* Advanced customer lifetime value analysis
* Campaign attribution modeling
* Cloud-based deployment
* Automated KPI alerts
* Advanced predictive analytics
* Interactive scenario analysis

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

## Deepa Saxena

**Data Analyst | Python | SQL | PostgreSQL | Power BI | DAX | Excel | Machine Learning**

📧 Email: [saxenadeepa103@gmail.com](mailto:saxenadeepa103@gmail.com)

🔗 GitHub: [Deepa2501](https://github.com/Deepa2501)

🔗 LinkedIn: [Deepa Saxena](https://www.linkedin.com/in/deepa-saxena-694082390/)

---

<p align="center">
  ⭐ If you found this project useful, consider giving it a star!
</p>
```
