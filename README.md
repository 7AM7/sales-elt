# Comprehensive ELT Sales Data Pipeline

<h1 align="center">
  <a
    target="_blank"
    href="https://mage.ai"
  >
    <img
      align="center"
      alt="Mage"
      src="https://github.com/mage-ai/assets/blob/main/mascots/mascots-shorter.jpeg?raw=true"
      style="width:100%;"
    />
  </a>
</h1>

## Overview
This project involves constructing an advanced sales data pipeline for a retail company, integrating sales data with user and weather information to facilitate comprehensive analysis of customer behavior and sales trends.

## Technology Stack
- **Python**: For scripting and automation of the pipeline.
- **[MageAI](https://docs.mage.ai/introduction/overview)**: For pipeline  orchestration, visualization and integrate and synchronize data from various sources.
- **[DBT (Data Build Tool)](https://www.getdbt.com/)**: For transforming data with SQL.
- **PostgreSQL**: As the relational database management system.

## Pipeline
- ### Pipeline Execution
    To run the pipeline, follow these steps:

    1. Clone the repository:
        ```
        git clone https://github.com/7AM7/sales-elt
        ```
    2. Navigate to the project directory:
        ```
        cd sales-elt
        ```
    3. Create a `.env` file in the project root directory with the following environment variables:
        ```
        POSTGRES_DB=postgres
        POSTGRES_USER=admin
        POSTGRES_PASSWORD=admin
        PG_HOST_PORT=5432
        POSTGRES_HOST=postgres-magic
        POSTGRES_SCHEMA=dbt_demo
        WEATHER_API_KEY={WEATHER_API_KEY}
        ```
        **NOTE**: To obtain your unique `WEATHER_API_KEY`, sign up or log in at [OpenWeatherMap](https://openweathermap.org/) and follow their instructions.

    4. Start the services using Docker:
        ```
        docker-compose up
        ```

    After running the Docker command, you will have access to the following:

    - **MageAI**: [http://localhost:6789/](http://localhost:6789/) - A web interface for managing, visualizing and transforming data.
    - **DBT Documentation**: [http://localhost:8001/](http://localhost:8001/) - Provides an overview of your DBT models, their lineage, and documentation.
    <br/>**Note**: You may need to refresh the page for DBT docs to load properly.

- ### Pipelines Workflow
  #### Sales ELT Pipeline
    - The following diagram represents the ELT pipeline implemented in this project:
      <h1 align="center">
        <a
          target="_blank"
          href="https://mage.ai"
        >
          <img
            align="center"
            alt="Mage"
            src="assets/pipeline_workflow.png"
            style="width:100%;"
          />
        </a>
      </h1>

      *Above image depicts the workflow of the ELT (Extract, Load, Transform) pipeline. It illustrates the processes from data extracting to loading and final transformation.*

  - **Data Extracting**:
      - Parallel extracting of sales (Local File) and user data (User API).
      - Retrieve weather information based on the user's geographical coordinates (latitude and longitude) through the specified weather data API endpoint.
      - Store the extracted data in the `archive/users`, `archive/sales`, and `archive/weather` directories, naming the files according to the pipeline execution timestamp in the format `year-month-day-hour.csv`.

  - **Data Loading**:
      - Load the data into three tables: `raw_user`, `raw_weather`, and `raw_sale`.
      - Initiate preliminary transformations by defining unique identifiers for sales and weather records to ensure data uniformity and integrity prior to the detailed transformation phase.

  - **Transformation**:
    - Data from `raw_user` is transformed and stored into `dim_user` with snapshot scehma to keep the user history.
    - Data from `raw_weather` is similarly transformed into `dim_weather`.
    - The transformation process include data cleaning and manipulation.
    - `fact_sales` is an incremental table created by joining `dim_user` and `dim_weather`. Only includes active records to reflect the most recent data and using the fact for reporting and visualizations.

  #### Sales Reporting and Visualizations Pipeline

  The Sales Reporting and Visualizations Pipeline is a sophisticated segment of our data system that utilizes DBT for executing a variety of aggregation queries on the `fact_sales` table. The purpose of this pipeline is to derive actionable business insights and facilitate data-driven decision-making. Below is a table detailing the business questions addressed, the visualizations used to present the data, and the insights or impacts derived from each analysis.
  <table width="100%" border="1">
    <thead>
      <tr>
        <th>Business Question</th>
        <th>Visualization Chart (Image)</th>
        <th>Business Answer/Insights/Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>What are the total sales per customer?</td>
        <td><img src="assets/total_sales_per_customer.png" alt="Total Sales Per Customer"></td>
        <td>Analysis of total sales per customer provides insights into customer value, helping to identify high-value customers and tailor marketing strategies to enhance customer loyalty and increase sales.</td>
      </tr>
      <tr>
        <td>What is the average order quantity per product?</td>
        <td><img src="assets/average_order_quantity_per_product.png" alt="Average Order Quantity Per Product"></td>
        <td>Insights into the most and least popular products based on order quantity can inform inventory management and marketing strategies.</td>
      </tr>
      <tr>
        <td>How do sales vary with weather conditions?</td>
        <td><img src="assets/average_sales_per_weather.png" alt="Average Sales Per Weather"></td>
        <td>Understanding the impact of weather on sales can guide promotions and stock adjustments.</td>
      </tr>
      <tr>
        <td>What is the product sales summary by city?</td>
        <td><img src="assets/city_product_sales_summary.png" alt="City Product Sales Summary"></td>
        <td>Identifying which products sell best in which cities can inform regional sales strategies.</td>
      </tr>
      <tr>
        <td>How has customer spending changed over time?</td>
        <td><img src="assets/customer_spend_over_time.png" alt="Customer Spend Over Time"></td>
        <td>Tracking spending trends over time can reveal customer loyalty and the effectiveness of long-term engagement efforts.</td>
      </tr>
      <tr>
        <td>Which products are likely to be reordered by customers?</td>
        <td><img src="assets/likely_to_be_ordered_again_products.png" alt="Likely To Be Ordered Again Products"></td>
        <td>Pinpointing products with high repeat purchase rates can influence stock ordering and product development.</td>
      </tr>
      <tr>
        <td>What are the monthly sales trends?</td>
        <td><img src="assets/sales_trends_monthly.png" alt="Sales Trends Monthly"></td>
        <td>Monthly sales trends provide insights into seasonal effects and can be used for forecasting.</td>
      </tr>
      <tr>
        <td>What are the quarterly sales trends?</td>
        <td><img src="assets/sales_trends_quarterly.png" alt="Sales Trends Quarterly"></td>
        <td>Understanding quarterly trends helps in setting short-term goals and adjusting tactics accordingly.</td>
      </tr>
      <tr>
        <td>Who are the top-selling customers?</td>
        <td><img src="assets/top_selling_customers.png" alt="Top Selling Customers"></td>
        <td>Identifying top customers can help in customizing loyalty programs and targeting marketing campaigns.</td>
      </tr>
      <tr>
        <td>What are the top-selling products?</td>
        <td><img src="assets/top_selling_products.png" alt="Top Selling Products"></td>
        <td>Knowing the bestsellers can assist in inventory prioritization and highlight successful product features.</td>
      </tr>
      <tr>
        <td>How do weekly sales vary per customer?</td>
        <td><img src="assets/weekly_sales_per_customer.png" alt="Weekly Sales Per Customer"></td>
        <td>Weekly sales data per customer can aid in personalizing sales approaches and optimizing contact times.</td>
      </tr>
    </tbody>
  </table>


## Database Schema
![Database Schema](/mnt/data/img.jpg)
The schema illustrates the data storage and transformation process, including archiving, versioning, and backfilling strategies.

## Data Quality and Documentation
- Run data quality checks using DBT tests.
- Generate and view documentation using `dbt docs` and `dbt serve`.

## Data versioning

## Conclusion
Designed to be scalable and adaptable, this pipeline forms a robust foundation for in-depth sales and customer behavior analytics.
