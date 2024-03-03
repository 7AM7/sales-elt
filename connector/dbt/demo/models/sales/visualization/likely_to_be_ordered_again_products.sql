{{
    config(
        materialized = "view"
    )
}}

WITH product_order_counts AS (
    SELECT
        product_id,
        COUNT(order_id) AS order_count,
        MAX(order_date) AS last_order_date
    FROM {{ ref('fact_sales') }}
    GROUP BY product_id
),

current_date_reference AS (
    SELECT
        CURRENT_DATE AS current_date

),

likelihood_score AS (
    SELECT
        poc.product_id,
        poc.order_count,
        poc.last_order_date,
        poc.order_count::FLOAT / NULLIF(current_date - poc.last_order_date, 0) AS likelihood_score
    FROM product_order_counts poc, current_date_reference cdr
    ORDER BY likelihood_score DESC
)

SELECT
    product_id,
    order_count,
    last_order_date,
    likelihood_score
FROM likelihood_score
