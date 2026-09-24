from src.s3_persistance import S3Persistance
from src.weather_api import GetApi
import logging
import json



params = {
	"latitude": 19.4326,
	"longitude": -99.1332,
	"current": "temperature_2m",
	"timezone": "auto",
}
url = "https://api.open-meteo.com/v1/forecast"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event,context):
    try:
        data = GetApi(url=url,params=params).connection()
        S3Persistance(bucket_name="weather_api_pipeline").upload_file(data=data,destination_key="data.json")
        logger.info(f"lambda {__name__} succesfully runned.")
    except Exception as e:
        logger.error(f"could not runned at {__name__}")
        raise e
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Data uploaded successfully"})
    }
