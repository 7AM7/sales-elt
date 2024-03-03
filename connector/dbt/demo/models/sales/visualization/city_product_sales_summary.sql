{{ config(materialized = 'view') }}

SELECT
    city,
    SUM(quantity) AS total_products_sold
FROM {{ ref('fact_sales') }}
GROUP BY city
ORDER BY total_products_sold DESC
