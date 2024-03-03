{{
    config(
        materialized = "view"
    )
}}

with sales_data as (
  select
    product_id,
    customer_id,
    quantity,
    price,
    quantity * price as total_sales
  from {{ ref('fact_sales') }}
)

, product_sales as (
  select
    product_id,
    sum(total_sales) as total_product_sales
  from sales_data
  group by product_id
  order by total_product_sales desc
)


, ranked_product_sales as (
  select
    product_id,
    total_product_sales,
    rank() over (order by total_product_sales desc) as product_rank
  from product_sales
)


select
  product_id,
  total_product_sales as total_sales,
  product_rank as rank
from ranked_product_sales
