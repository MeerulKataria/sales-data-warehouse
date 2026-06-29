SELECT

    category,

    ROUND(SUM(total_sales),2) AS total_sales,

    ROUND(SUM(total_profit),2) AS total_profit,

    ROUND(
        (SUM(total_profit) / NULLIF(SUM(total_sales),0)) * 100,
        2
    ) AS profit_margin_percent

FROM vw_product_performance

GROUP BY category

ORDER BY profit_margin_percent DESC;