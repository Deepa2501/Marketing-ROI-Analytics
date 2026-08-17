# 📊 Marketing ROI Analytics Dashboard

An end-to-end Marketing ROI Analytics project that transforms raw marketing campaign data into actionable business insights using Python, PostgreSQL, SQL, and Power BI.

This project demonstrates the complete analytics lifecycle—from data cleaning and ETL to database management, SQL analysis, KPI development, and interactive business dashboards.

---

# 🚀 Project Overview

Marketing teams often struggle to understand which campaigns generate the highest return on investment and customer engagement.

This project solves that problem by building a complete Business Intelligence solution that enables users to:

- Monitor campaign performance
- Analyze marketing ROI
- Track customer engagement
- Compare campaign effectiveness
- Identify top-performing customer segments
- Generate executive-level business insights

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Data Cleaning | Pandas, NumPy |
| Database | PostgreSQL |
| SQL | PostgreSQL SQL |
| Visualization | Power BI |
| ETL | Python |
| Version Control | Git & GitHub |
| Source Data | Excel (.xlsx) |

---

# 📂 Project Structure

```text
Marketing-ROI-Analytics/
│
├── 📁 data/
│   ├── 📁 raw/                  # Raw marketing campaign data
│   └── 📁 cleaned/              # Cleaned & analysis-ready data
│
├── 📁 python/                   # Python analytics & ML pipeline
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
├── 📁 sql/                      # PostgreSQL database & analytics
│   ├── schema.sql
│   ├── analysis.sql
│   ├── advanced_analysis.sql
│   └── kpi_queries.sql
│
├── 📁 powerbi/
│   └── Marketing_ROI_Analytics.pbix
│
├── 📁 screenshots/              # Power BI dashboard previews
│   ├── executive_overview.png
│   ├── campaign_performance.png
│   └── Customer_&_Marketing_Insights.png
│
├── 📁 reports/                  # Generated analytics & ML outputs
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
├── 📁 dashboard/                # Dashboard workspace
├── 📁 excel/                   # Excel analysis workspace
├── 📁 images/                  # Supporting project images
├── 📁 ml/                      # Machine Learning workspace
└── 📁 workflow/                # Project workflow resources
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 LICENSE
├── 📄 .gitignore
└── 📄 data - Shortcut.lnk
```

---

# 🔄 ETL Workflow

```text
Raw Excel Dataset
        │
        ▼
Python Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Clean Dataset
        │
        ▼
PostgreSQL Database
        │
        ▼
SQL Analysis
        │
        ▼
Power BI Dashboard
```

---

# 🗄 Database Schema

Table Name

```text
marketing_campaigns
```

Columns

- Campaign_ID
- Campaign_Type
- Target_Audience
- Duration
- Channel_Used
- Impressions
- Clicks
- Leads
- Conversions
- Revenue
- Acquisition_Cost
- ROI
- Language
- Engagement_Score
- Customer_Segment
- Date

---

# 📈 SQL Analysis

The project includes more than **35 SQL queries** covering:

- Total Revenue
- Average ROI
- Campaign Performance
- Revenue by Marketing Channel
- Revenue by Customer Segment
- Monthly Revenue
- Conversion Rate Analysis
- Window Functions
- Ranking Queries
- Subqueries
- Advanced SQL Analytics

---

# 📊 Power BI Dashboard

## 📄 Dashboard 1 — Executive Overview

Features

- KPI Cards
- Revenue Trend
- Revenue by Campaign Type
- Revenue by Marketing Channel
- Customer Segment Analysis
- Top Campaigns
- Interactive Filters

>  ![Executive Overview Dashboard](screenshots/executive_overview.png)

---

## 📄 Dashboard 2 — Campaign Performance

Features

- Campaign Performance
- Marketing Channel Analysis
- Language Analysis
- Target Audience Performance
- ROI Comparison
- Engagement Analysis

> ![Campaign Performance Dashboard](screenshots/campaign_performance.png)

---

## 📄 Dashboard 3 — Customer & Marketing Insights

Features

- Marketing Funnel
- ROI Distribution
- Customer Segment Performance
- Revenue Trend
- Channel Performance Matrix
- Executive Business Insights

> ![Customer & Marketing Insights Dashboard](screenshots/Customer_&_Marketing_Insights.png)

---

# 📌 Key KPIs

- Total Revenue
- Average ROI
- Total Campaigns
- CTR
- Conversion Rate
- CPA
- Average Revenue
- Average Engagement
- Total Customers
- Funnel Conversion Rate

---

# 💡 Key Business Insights

- Social Media campaigns generated the highest ROI.
- Premium customer segments contributed the largest revenue.
- Marketing funnel highlights opportunities to improve conversions.
- Customer engagement positively impacts campaign performance.
- Language-specific campaigns influence revenue distribution.
- High-performing channels should receive increased marketing investment.

---

# 📈 Business Value

This dashboard helps marketing teams to:

- Improve campaign ROI
- Optimize marketing spend
- Increase customer engagement
- Monitor campaign performance
- Support data-driven business decisions

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Deepa2501/Marketing-ROI-Analytics.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute ETL

```bash
python python/etl.py
```

### Import Data into PostgreSQL

Execute

```text
schema.sql
```

### Open Dashboard

Open

```text
Marketing_ROI_Analytics.pbix
```

using Microsoft Power BI Desktop.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Deepa Saxena**

Data Analyst | Python | SQL | PostgreSQL | Power BI | Excel | Machine Learning

GitHub: https://github.com/Deepa2501

LinkedIn: https://www.linkedin.com/in/deepa-saxena-694082390/