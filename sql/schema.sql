DROP TABLE IF EXISTS marketing.marketing_campaigns;

CREATE TABLE marketing.marketing_campaigns (
    campaign_id VARCHAR(20),
    campaign_type VARCHAR(50),
    target_audience VARCHAR(100),
    duration INT,
    channel_used VARCHAR(100),
    impressions INT,
    clicks INT,
    leads INT,
    conversions INT,
    revenue NUMERIC(12,2),
    acquisition_cost NUMERIC(12,2),
    roi NUMERIC(8,2),
    language VARCHAR(50),
    engagement_score NUMERIC(8,2),
    customer_segment VARCHAR(100),
    campaign_date DATE
);