{{
    config(
        materialized = "view"
    )
}}
WITH sales_data AS (
    SELECT
        customer_id,
        SUM(quantity * price) AS total_sales_amount
    FROM
        {{ ref('fact_sales') }}
    GROUP BY
        customer_id
)

SELECT
    customer_id,
    total_sales_amount
FROM
    sales_data
ORDER BY
    total_sales_amount DESC
