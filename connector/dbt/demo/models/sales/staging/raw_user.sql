{{ config(materialized='table') }}

WITH raw_users AS (
  SELECT
  *
  FROM
    {{ source('mage_demo', 'sales_pipeline_load_user_data') }}
)

SELECT
id AS user_id,
name,
username,
email,
phone,
website,
"address.street",
"address.suite",
"address.city",
"address.zipcode",
"address.geo.lat",
"address.geo.lng",
"company.name",
"company.catchPhrase",
"company.bs"
FROM raw_users
