{% snapshot dim_user %}

{{ config(
    target_schema='snapshots',
    unique_key='user_id',
    strategy='check',
    check_cols=['user_id']
) }}


SELECT
  user_id,
  name,
  username,
  email,
  "address.geo.lat" AS lat,
  "address.geo.lng" AS lng,
  "address.city" AS city
   FROM {{ ref('raw_user') }}
{% endsnapshot %}
