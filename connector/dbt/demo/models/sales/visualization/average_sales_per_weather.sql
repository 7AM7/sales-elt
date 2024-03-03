{{
    config(
        materialized = 'view'
    )
}}

WITH weather_sales AS (
  SELECT
    weather_conditions,
    SUM(price * quantity) AS total_sales,
    AVG(price * quantity) AS average_sales_amount,
    COUNT(*) AS number_of_transactions
  FROM {{ ref('fact_sales') }}
  GROUP BY weather_conditions
)

SELECT
  weather_conditions,
  total_sales,
  average_sales_amount,
  number_of_transactions
FROM weather_sales
ORDER BY average_sales_amount DESC
