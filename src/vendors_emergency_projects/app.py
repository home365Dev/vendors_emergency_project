import logging

import json
import pandas as pd
import requests

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
    project_id_str = data['project_id']
    row_df = pd.DataFrame(columns=[config.PROJECT_ID, config.TEXT, config.EMERGENCY])
    row_df = row_df.append({config.PROJECT_ID: project_id_str, config.TEXT: input_str}, ignore_index=True)
    try:
        result_df = run(row_df)
        result_to_dict = {
            config.EMERGENCY: result_df[config.EMERGENCY][0],
            config.IS_EMERGENCY: result_df[config.IS_EMERGENCY][0]
        }
        if result_to_dict[config.IS_EMERGENCY]:
            emer = "EMERGENCY"
        else:
            emer = "NORMAL"
        req1 = {
            "leadId": project_id_str,
            "classification": emer
        }
        req = json.dumps(req1).replace("\'", "\"")
        url = "https://app-dev.home365.co/projects-service-dev/projects/update-project?userId=495e020a-7af6-4381-a665-3c16d5ce4c1c"
        payload = req
        headers = {
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return result_to_dict
    except Exception as e:
        logger.error(json.dumps({'error': str(e)}))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
             }

if __name__ == '__main__':
    jst = { "text": "all right , I m probably gon na regret order point , soon possible master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine", 'project_id': 'c5c6ba50-245f-4be1-aab8-5c68dac1bb64'}
    result = execute(jst)
    print(result)