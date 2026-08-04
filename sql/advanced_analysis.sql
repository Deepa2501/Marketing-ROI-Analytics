-- Query 1 — Top 3 Campaigns in Each Marketing Channel
-- Business Question
-- Which are the top 3 revenue-generating campaigns within each marketing channel?

SELECT *
FROM (
    SELECT
        campaign_id,
        channel_used,
        revenue,
        ROW_NUMBER() OVER (
            PARTITION BY channel_used
            ORDER BY revenue DESC
        ) AS rank
    FROM marketing.marketing_campaigns
) ranked
WHERE rank <= 3;

-- Query 2 — Monthly Revenue Growth
-- Business Question
-- How has revenue changed compared to the previous month?

WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', date) AS month,
        SUM(revenue) AS revenue
    FROM marketing.marketing_campaigns
    GROUP BY month
)

SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_growth
FROM monthly_revenue;

-- Query 3 — Running Revenue
-- Business Question
-- What is the cumulative revenue over time?

SELECT
    DATE_TRUNC('month', date) AS month,
    SUM(revenue) AS monthly_revenue,

    SUM(SUM(revenue)) OVER (
        ORDER BY DATE_TRUNC('month', date)
    ) AS cumulative_revenue

FROM marketing.marketing_campaigns
GROUP BY month
ORDER BY month;

-- Query 4 — Best Performing Month
-- Business Question
-- Which month generated the highest revenue?

SELECT
DATE_TRUNC('month', date) AS month,
SUM(revenue) total_revenue
FROM marketing.marketing_campaigns
GROUP BY month
ORDER BY total_revenue DESC
LIMIT 1;

-- Query 5 — Worst Performing Month
-- Business Question
-- Which month generated the lowest revenue?

SELECT
DATE_TRUNC('month', date) AS month,
SUM(revenue) total_revenue
FROM marketing.marketing_campaigns
GROUP BY month
ORDER BY total_revenue
LIMIT 1;

-- Query 6 — Campaigns Above Average ROI (CTE)
-- Business Question
-- Which campaigns performed better than the overall average ROI?

WITH avg_roi AS (
SELECT AVG(roi) average_roi
FROM marketing.marketing_campaigns
)

SELECT
campaign_id,
campaign_type,
roi
FROM marketing.marketing_campaigns,
avg_roi
WHERE roi > average_roi;

-- Query 7 — Top 20% Campaigns
-- Business Question
-- Which campaigns belong to the top 20% based on revenue?

SELECT *
FROM (
SELECT
campaign_id,
campaign_type,
revenue,
NTILE(5) OVER(
ORDER BY revenue DESC
) bucket
FROM marketing.marketing_campaigns
) t

WHERE bucket = 1;

-- Query 8 — Revenue Contribution %
-- Business Question
-- What percentage of total revenue does each campaign contribute?

SELECT
campaign_id,
revenue,
ROUND(
revenue *100.0/
SUM(revenue) OVER(),
4
) contribution_percentage

FROM marketing.marketing_campaigns
ORDER BY contribution_percentage DESC;

-- Query 9 — Campaign Performance Category
-- Business Question
-- How can campaigns be classified based on ROI?

SELECT
campaign_id,
campaign_type,
roi,
CASE
WHEN roi>=8 THEN 'Excellent'
WHEN roi>=5 THEN 'Good'
WHEN roi>=2 THEN 'Average'
ELSE 'Poor'
END performance

FROM marketing.marketing_campaigns;

-- Query 10 — Executive KPI Summary
-- Business Question
-- What are the overall marketing KPIs in one summary table?


SELECT

COUNT(*) total_campaigns,

SUM(revenue) total_revenue,

ROUND(AVG(roi)::NUMERIC,2) average_roi,

ROUND(
SUM(clicks)::NUMERIC/
SUM(impressions)*100,
2
) ctr,

ROUND(
SUM(conversions)::NUMERIC/
SUM(clicks)*100,
2
) conversion_rate,

ROUND(
SUM(acquisition_cost)::NUMERIC/
SUM(conversions),
2
) cpa

FROM marketing.marketing_campaigns;