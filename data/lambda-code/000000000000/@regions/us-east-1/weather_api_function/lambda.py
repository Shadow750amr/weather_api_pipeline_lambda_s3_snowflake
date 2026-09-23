from src.s3_persistance import S3Persistance
from src.weather_api import GetApi
import logging



params = {
	"latitude": 19.4326,
	"longitude": -99.1332,
	"current": "temperature_2m",
	"timezone": "auto",
}
url = "https://api.open-meteo.com/v1/forecast"


def lambda_handler(event,context):
    """
    Main Lambda handler function
    Parameters:
        event: Dict containing the Lambda function event data
        context: Lambda runtime context
    Returns:
        Dict containing status message
    """
    data = GetApi(url=url,params=params).connection()
    S3Persistance(bucket_name="weather_api_pipeline").upload_file(data=data,destination_key="data.json")

