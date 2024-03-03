{% snapshot dim_weather %}

{{ config(
    target_schema='snapshots',
    unique_key='weather_id',
    strategy='check',
    check_cols=['weather_lat', 'weather_lng']
) }}


SELECT
    weather_id,
    weather_date,
    weather_lat,
    weather_lng,
    weather_temperature,
    weather_conditions
   FROM {{ ref('raw_weather') }}
{% endsnapshot %}
