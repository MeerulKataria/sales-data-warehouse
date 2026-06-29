SELECT
    product_name,
    category,
    total_sales,
    total_profit
FROM vw_product_performance
ORDER BY total_sales DESC
LIMIT 10;