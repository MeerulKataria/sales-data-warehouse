SELECT

    year,
    month,
    month_name,
    total_sales,

    SUM(total_sales)
    OVER(
        ORDER BY year, month
    ) AS running_total_sales

FROM vw_monthly_sales;