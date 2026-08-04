-- KPI 1 — Click Through Rate (CTR)
-- Business Question
-- Which campaign type gets the highest click-through rate?
SELECT
campaign_type,
ROUND(
(SUM(clicks)::NUMERIC / SUM(impressions)) * 100,
2
) AS ctr_percentage
FROM marketing.marketing_campaigns
GROUP BY campaign_type
ORDER BY ctr_percentage DESC;

-- KPI 2 — Conversion Rate
-- Business Question
-- Which campaign type converts the most visitors into customers?
SELECT
campaign_type,
ROUND(
(SUM(conversions)::NUMERIC / SUM(clicks)) * 100,
2
) AS conversion_rate
FROM marketing.marketing_campaigns
GROUP BY campaign_type
ORDER BY conversion_rate DESC;

-- KPI 3 — Cost Per Click (CPC)
-- Business Question
-- Which campaign type spends the least per click?
SELECT
campaign_type,
ROUND(
SUM(acquisition_cost)::NUMERIC /
SUM(clicks),
2
) AS cost_per_click
FROM marketing.marketing_campaigns
GROUP BY campaign_type
ORDER BY cost_per_click;

-- KPI 4 — Cost Per Acquisition (CPA)
-- Business Question
-- Which campaign type acquires customers at the lowest cost?
SELECT
campaign_type,
ROUND(
SUM(acquisition_cost)::NUMERIC /
SUM(conversions),
2
) AS cost_per_acquisition
FROM marketing.marketing_campaigns
GROUP BY campaign_type
ORDER BY cost_per_acquisition;

-- KPI 5 — Revenue Per Conversion
-- Business Question
-- Which campaign type generates the highest revenue per converted customer?
SELECT
campaign_type,
ROUND(
SUM(revenue)::NUMERIC /
SUM(conversions),
2
) AS revenue_per_conversion
FROM marketing.marketing_campaigns
GROUP BY campaign_type
ORDER BY revenue_per_conversion DESC;

-- KPI 6 — Average ROI by Channel
-- Business Question
-- Which marketing channel provides the best return on investment (ROI)?
SELECT
channel_used,
ROUND(AVG(roi)::NUMERIC,2) AS avg_roi
FROM marketing.marketing_campaigns
GROUP BY channel_used
ORDER BY avg_roi DESC;

-- KPI 7 — Best Customer Segment
-- Business Question
-- Which customer segment provides the best return on investment (ROI)?
SELECT
customer_segment,
ROUND(AVG(roi)::NUMERIC,2) AS avg_roi
FROM marketing.marketing_campaigns
GROUP BY customer_segment
ORDER BY avg_roi DESC;

-- KPI 8 — Best Language
-- Business Question
-- Which language provides the best return on investment (ROI)?
SELECT
language,
ROUND(AVG(roi)::NUMERIC,2) AS avg_roi
FROM marketing.marketing_campaigns
GROUP BY language
ORDER BY avg_roi DESC;

-- KPI 9 — Monthly Campaign Count
-- Business Question
-- How many campaigns are run each month?
SELECT
DATE_TRUNC('month',date) AS month,
COUNT(*) AS campaigns
FROM marketing.marketing_campaigns
GROUP BY month
ORDER BY month;

-- KPI 10 — Top 5 Most Profitable Campaigns
-- Business Question
-- Which campaigns are the most profitable?
SELECT
campaign_id,
campaign_type,
revenue,
roi
FROM marketing.marketing_campaigns
ORDER BY roi DESC,revenue DESC
LIMIT 5;