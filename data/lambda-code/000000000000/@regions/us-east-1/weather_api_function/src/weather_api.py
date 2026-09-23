import requests
import logging
import json
import boto3

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

params = {
	"latitude": 19.4326,
	"longitude": -99.1332,
	"current": "temperature_2m",
	"timezone": "auto",
}
url = "https://api.open-meteo.com/v1/forecast"


class GetApi:
    
    def __init__(self,*,url,params):
        self.url = url

        self.params = params
        logger.info("Class initialized")
    def connection(self):
        try:
            req = requests.get(url=self.url,params=self.params)
            req.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"an error occurred during data capture {e}")
            raise
        else:
            logger.info(f"Process done for {self.__class__}")
            return json.dumps(req.json())


if __name__=="__main__":
    ini = GetApi(url=url,params=params)
    ini.connection()



