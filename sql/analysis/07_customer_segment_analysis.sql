SELECT
    segment,
    COUNT(*) AS total_customers,
    ROUND(SUM(total_sales),2) AS total_sales,
    ROUND(SUM(total_profit),2) AS total_profit
FROM vw_customer_analysis
GROUP BY segment
ORDER BY total_sales DESC;