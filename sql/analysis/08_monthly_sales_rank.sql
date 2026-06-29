SELECT
    year,
    month_name,
    total_sales,

    RANK() OVER(
        ORDER BY total_sales DESC
    ) AS sales_rank

FROM vw_monthly_sales;