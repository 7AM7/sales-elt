{{
    config(
        materialized = "view"
    )
}}

WITH monthly_sales AS (
  SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(quantity * price) AS total_sales,
    AVG(quantity * price) AS average_sale_amount,
    COUNT(*) AS number_of_transactions
  FROM {{ ref('fact_sales') }}
  GROUP BY DATE_TRUNC('month', order_date)
  ORDER BY month
)

SELECT
  month,
  total_sales,
  average_sale_amount,
  number_of_transactions
FROM monthly_sales
