import logging

import json
import pandas as pd
from src.vendors_emergency_projects.emergency_checker import run
import src.vendors_emergency_projects.config as config
LOGGER = logging.getLogger(__name__)

def execute(data: dict):
    LOGGER.info("Hello World")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info('event parameter: {}'.format(data))
    # print("Received event: " + json.dumps(event, indent=2))
    my_json_str = json.dumps(data)
    logger.info('event parameter: {}'.format(my_json_str))

    input_str = data['text']
    row_df = pd.DataFrame(columns=[config.TEXT_TITLE, config.CLEAN_TITLE, config.FIXED_TITLE, config.EMERGENCY])
    row_df = row_df.append({config.CLEAN_TITLE: input_str}, ignore_index=True)
    try:
        return run(row_df)
    except Exception as e:
        logger.error(e)
        print(json.dumps({'error': str(e)}))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
             }