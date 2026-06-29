DROP VIEW IF EXISTS vw_product_performance;

CREATE VIEW vw_product_performance AS

SELECT

    p.product_name,
    p.category,
    p.sub_category,

    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    SUM(f.quantity) AS total_quantity,
    AVG(f.discount) AS avg_discount

FROM fact_sales f

JOIN dim_product p
    ON f.product_key = p.product_key

GROUP BY

    p.product_name,
    p.category,
    p.sub_category

ORDER BY

    total_sales DESC;