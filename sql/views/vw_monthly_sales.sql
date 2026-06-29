DROP VIEW IF EXISTS vw_monthly_sales;

CREATE VIEW vw_monthly_sales AS

SELECT

    d.year,
    d.month,
    d.month_name,

    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    SUM(f.quantity) AS total_quantity,
    COUNT(*) AS total_orders

FROM fact_sales f

JOIN dim_date d
    ON f.date_key = d.date_key

GROUP BY

    d.year,
    d.month,
    d.month_name

ORDER BY

    d.year,
    d.month;