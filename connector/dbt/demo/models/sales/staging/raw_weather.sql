{{ config(materialized='table') }}

WITH raw_weathers AS (
  SELECT
  {{ dbt_utils.generate_surrogate_key(['weather_lat', 'weather_lng']) }} AS weather_id,
    *
  FROM
    {{ source('mage_demo', 'sales_pipeline_prepare_weather_data') }}
)

SELECT * FROM raw_weathers
