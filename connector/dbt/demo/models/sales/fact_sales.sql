{{ config(
    materialized='incremental',
    unique_key='sale_id'
) }}

WITH fact_sale AS (
  SELECT
    "sale_id",
    "order_id",
    "customer_id",
    "product_id",
    "quantity",
    "price",
    "order_date"
  FROM
    {{ ref('raw_sale') }}
)

SELECT
fs.sale_id,
fs.order_id,
fs.customer_id,
fs.product_id,
dw.weather_id,
fs.order_date,
fs.quantity,
fs.price,
du.city,
dw.weather_temperature,
dw.weather_conditions
FROM
fact_sale as fs
inner join {{ ref('dim_user') }} as du on fs.customer_id=du.user_id
inner join {{ ref('dim_weather') }} as dw on du.lat=dw.weather_lat and du.lng=dw.weather_lng

{% if is_incremental() %}

  where order_date >= (select max(order_date) from {{ this }})
  and du.dbt_valid_to is null
  and du.dbt_valid_to is null

{% endif %}
