### WEATHER MICROBATCH PIPELINE USING AWS LAMBDA, AWS S3, AWS EVENT BRIDGE AND SNOWFLAKE AS DWH

The main purpose of this project is to desing and build a **serverless project** using state of the art tools for managing **microbatch pipelines**.
The scope in this case is to get data from a known API called **open-meteo** which serves different weather mesures such as humidity, rain precipitation, temperature, among other indicators.
The very final objetive of this project is to show the application benefits of such implementation.

## Tools used for this project

Important to say this project was implemented using **https://floci.io/**, a local emulator for cloud enviroments that works well with most functions and integrations for serverless projects prototypes. Also, it uses the AWS CLI that pretty much is the most essential needed toll for dev and test functions, buckets and IAM configurations.

* **Event Bridge Scheduler:** AWS EventBridge triggers execution at fixed cron intervals.
* **Lambda:** AWS Lambda fetches Open-Meteo metrics (temperature) and formats raw JSON payloads.
* **S3:** Amazon S3 stores raw payloads in a partitioned hive-style folder structure (`year=YYYY/month=MM/`).
* **Snowflake:** Snowflake ingests S3 objects into a raw `VARIANT` stage and materializes structured analytical models.


## Configuration
 ### 
    1. Make sure to have docker desktop installed on your computer.
    2. Make sure to have AWS CLI installed on your computer.

To clon this repo just run the following steps:

1. Run git clone https://github.com/Shadow750amr/weather_api_pipeline_lambda_s3_snowflake.git
2. Run docker compose up -d
3. Make sure everything is working properly

