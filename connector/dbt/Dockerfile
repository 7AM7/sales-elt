FROM python:3.10.7-slim as base
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

WORKDIR /usr/app/dbt/

FROM base as application
COPY demo /usr/app/dbt/

RUN python -m pip install --no-cache-dir dbt-postgres==1.7.9

EXPOSE 8001

ENTRYPOINT ["dbt"]
CMD ["docs", "serve", "--port", "8001"]
