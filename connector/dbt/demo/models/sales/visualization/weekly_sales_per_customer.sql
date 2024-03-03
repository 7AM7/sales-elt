{{
    config(
        materialized = "view"
    )
}}

WITH weekly_sales AS (
    SELECT
        customer_id,
        DATE_TRUNC('week', order_date) AS week_start_date,
        SUM(quantity * price) AS total_sales_amount
    FROM
        {{ ref('fact_sales') }}
    GROUP BY
        customer_id,
        week_start_date
)

SELECT
    customer_id,
    week_start_date,
    total_sales_amount
FROM
    weekly_sales
ORDER BY
    customer_id, week_start_date
