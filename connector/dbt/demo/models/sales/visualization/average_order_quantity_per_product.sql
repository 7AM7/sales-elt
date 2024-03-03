{{
    config(
        materialized = "view"
    )
}}

with base as (
  select
    product_id,
    quantity
  from {{ ref('fact_sales') }}
)

, aggregated_data as (
  select
    product_id,
    avg(quantity) as average_quantity
  from base
  group by product_id
)

select
  product_id,
  average_quantity
from aggregated_data
order by product_id
