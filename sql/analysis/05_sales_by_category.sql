SELECT
    category,
    ROUND(SUM(total_sales), 2) AS total_sales,
    ROUND(SUM(total_profit), 2) AS total_profit
FROM vw_product_performance
GROUP BY category
ORDER BY total_sales DESC;