# import watchtower
import logging
from logging import *
import src.vendors_emergency_projects.config as config

name_str = '[{}]'.format(str(config.ENV_PREFIX))
basicConfig(
    format='{} %(asctime)s %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s'.format(name_str),
    datefmt='%H:%M:%S',
    level=INFO)

logger = getLogger(__name__)
# logger.addHandler(StreamHandler(stream=sys.stdout))
# if not config.IS_TEST:
#     logger.addHandler(watchtower.CloudWatchLogHandler())

if config.IS_TEST:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
logger.info("Log has started")
