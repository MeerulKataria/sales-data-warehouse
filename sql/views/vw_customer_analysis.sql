DROP VIEW IF EXISTS vw_customer_analysis;

CREATE VIEW vw_customer_analysis AS

SELECT

    c.customer_name,
    c.segment,

    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    SUM(f.quantity) AS total_quantity,
    COUNT(*) AS total_orders

FROM fact_sales f

JOIN dim_customer c
    ON f.customer_key = c.customer_key

GROUP BY

    c.customer_name,
    c.segment

ORDER BY

    total_sales DESC;