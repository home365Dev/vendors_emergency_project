import watchtower
from logging import *
import src.vendors_emergency_projects.config as config

basicConfig(
    format='%(asctime)s %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S',
    level=INFO)

logger = getLogger(__name__)
# logger.addHandler(StreamHandler(stream=sys.stdout))
if not config.IS_TEST:
    logger.addHandler(watchtower.CloudWatchLogHandler())
logger.setLevel(config.LOG_LEVEL)
logger.info("Log has started")
