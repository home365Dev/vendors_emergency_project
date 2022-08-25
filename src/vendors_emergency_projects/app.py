import logging

import json
import pandas as pd
from src.vendors_emergency_projects.emergency_checker import run
LOGGER = logging.getLogger(__name__)
def execute(data: dict):
    LOGGER.info("Hello World")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info('event parameter: {}'.format(data))
    # print("Received event: " + json.dumps(event, indent=2))
    body = pd.DataFrame.from_dict(data)
    print("Received body:  " + str(body))
    try:
        return run(body)
    except Exception as e:
        logger.error(e)
        print(json.dumps({'error': str(e)}))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }