{{
    config(
        materialized = "view"
    )
}}


WITH quarterly_sales AS (
  SELECT
    DATE_TRUNC('quarter', order_date) AS quarter,
    SUM(quantity * price) AS total_sales,
    AVG(quantity * price) AS average_sale_amount,
    COUNT(*) AS number_of_transactions
  FROM {{ ref('fact_sales') }}
  GROUP BY DATE_TRUNC('quarter', order_date)
  ORDER BY quarter
)

SELECT
  quarter,
  total_sales,
  average_sale_amount,
  number_of_transactions
FROM quarterly_sales
