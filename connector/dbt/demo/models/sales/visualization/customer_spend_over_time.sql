{{ config(materialized = 'view') }}

WITH customer_spend AS (
  SELECT
    customer_id,
    order_date,
    SUM(quantity * price) AS total_spend
  FROM {{ ref('fact_sales') }}
  GROUP BY customer_id, order_date
)

SELECT
  customer_id,
  order_date,
  total_spend
FROM customer_spend
ORDER BY customer_id, order_date
