from src.s3_persistance import S3Persistance
from src.weather_api import GetApi
import logging
import json
from datetime import datetime


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

    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    timestamp_filename = datetime.now().strftime("%H%M%S")

    destination_key = (f"weather_api_current/year={year}/month={month}/day={day}/weather_{timestamp_filename}.json")

    try:
        data = GetApi(url=url,params=params).connection()
        S3Persistance(bucket_name="weather_api_pipeline").upload_file(data=data,destination_key=destination_key)
        logger.info(f"lambda {__name__} succesfully runned.")
    except Exception as e:
        logger.error(f"could not runned at {__name__}")
        raise e
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Data uploaded successfully"})
    }
