DROP VIEW IF EXISTS vw_sales_summary;

CREATE VIEW vw_sales_summary AS

SELECT

    f.sale_key,
    d.full_date,
    c.customer_name,
    c.segment,
    p.product_name,
    p.category,
    p.sub_category,
    f.sales,
    f.quantity,
    f.discount,
    f.profit

FROM fact_sales f

JOIN dim_customer c
    ON f.customer_key = c.customer_key

JOIN dim_product p
    ON f.product_key = p.product_key

JOIN dim_date d
    ON f.date_key = d.date_key;