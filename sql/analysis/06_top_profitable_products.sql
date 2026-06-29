SELECT
    product_name,
    category,
    total_profit
FROM vw_product_performance
ORDER BY total_profit DESC
LIMIT 10;