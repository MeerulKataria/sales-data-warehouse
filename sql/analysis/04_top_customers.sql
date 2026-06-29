SELECT
    customer_name,
    segment,
    total_sales,
    total_profit
FROM vw_customer_analysis
ORDER BY total_sales DESC
LIMIT 10;