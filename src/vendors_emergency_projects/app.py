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
    my_json_str = json.dumps(data)
    logger.info('event parameter: {}'.format(my_json_str))
    print("Received body:  " + str(my_json_str))

    body = data['text']
    rowdf = pd.DataFrame({'Object Key': ['1'], 'Category': ['Rami'], 'file_path': ['rami'], 'text': [body], 'object': ['000']})
    print("Received body:  " + str(body))
    try:
        return run(rowdf)
    except Exception as e:
        logger.error(e)
        print(json.dumps({'error': str(e)}))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
             }