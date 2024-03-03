{{ config(materialized='table') }}

WITH raw_sale AS (
  SELECT
   {{ dbt_utils.generate_surrogate_key(['cast(order_id as text)', 'product_id']) }} AS sale_id,
    order_id,
    customer_id,
    product_id,
    quantity,
    price,
    order_date
  FROM
    {{ source('mage_demo', 'sales_pipeline_load_sales_data') }}
)

SELECT * FROM raw_sale
