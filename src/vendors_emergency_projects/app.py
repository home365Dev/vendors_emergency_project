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
    row_df = pd.DataFrame(columns=[config.TEXT, config.EMERGENCY])
    row_df = row_df.append({config.TEXT: input_str}, ignore_index=True)
    try:
        result_df = run(row_df)
        result_to_dict = result_df.to_dict(orient='records')
        # result_to_dict_ext = {"1": result_to_dict}

        # result_json_struct = json.loads(result_df.to_json(orient="records"))
        # result_to_dict_ext = {"1": result_json_struct}
        # result_json = json.dumps(result_to_dict_ext, indent=3)
        return result_to_dict
    except Exception as e:
        # logger.error(e)
        logger.error(json.dumps({'error': str(e)}))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
             }

if __name__ == '__main__':
    jst = { "text": "all right , I m probably gon na regret order point , soon possible master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine"}
    result = execute(jst)
    print(result)