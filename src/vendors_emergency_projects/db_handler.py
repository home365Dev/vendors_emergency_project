import src.vendors_emergency_projects.db_connections as db
import json
import datetime
from src.vendors_emergency_projects.logger import logger
import src.vendors_emergency_projects.config as config
prefix = "_dev" if config.IS_TEST else ""



def execute_to_db(**kwargs):
    logger.info("execute_to_db: ")
    ts = datetime.datetime.now()
    # response
    res = kwargs.get('res_to_dict', {})
    id = kwargs.get('id', {})
    # json_input
    text = kwargs.get('text_of_case', {})

    postgres_insert_query = """ INSERT INTO {}
    (project_id, emergency_term, is_emergency, text_project, created_date)
    VALUES (%s, %s, %s, %s, %s)""".format("vendors_emergency_logs" + prefix)
    record_to_insert = (id, res[config.EMERGENCY], res[config.IS_EMERGENCY], text, ts)

    conn = db.connectToPost()
    cursor = conn.cursor()
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()
    conn.close()

    logger.info("execute_to_db is done")

