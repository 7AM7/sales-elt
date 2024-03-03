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

, customer_sales as (
  select
    customer_id,
    sum(total_sales) as total_customer_sales
  from sales_data
  group by customer_id
  order by total_customer_sales desc
)

, ranked_customer_sales as (
  select
    customer_id,
    total_customer_sales,
    rank() over (order by total_customer_sales desc) as customer_rank
  from customer_sales
)

select
  customer_id,
  total_customer_sales as total_sales,
  customer_rank as rank
from ranked_customer_sales
