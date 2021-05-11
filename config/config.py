import logging
import os
from pathlib import Path

from campuslibs.utilities.config import ConfigLoader
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_project_root():
    """Returns project root folder."""
    return str(Path(__file__).parent.parent) + '/'


env_path = get_project_root() + '.env'
try:
    logger.info(f"ENV PATH: {env_path}")
    load_dotenv(dotenv_path=env_path, verbose=False)
except:
    logger.info(f"{env_path} file not found!")


class Config(object):
    ENV = os.getenv("ENV", "dev")  # [dev, staging, production]
    SERVICE_NAME = os.getenv("SERVICE_NAME", "mindedge_transformer")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
    AWS_CONFIG_BUCKET = os.getenv("AWS_CONFIG_BUCKET")

    LOADER = ConfigLoader(ENV, SERVICE_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_CONFIG_BUCKET)
    CONFIG = LOADER.get_configs()

    if not CONFIG:
        logger.error("Config not loaded. Use correct AWS values")
        raise Exception('Config not found')

    # Mongo
    MONGODB_DATABASE = CONFIG["mongodb_database"]
    MONGODB_HOST = CONFIG["mongodb_host"]
    MONGODB_PORT = int(CONFIG["mongodb_port"])
    MONGODB_USERNAME = CONFIG["mongodb_username"]
    MONGODB_PASSWORD = CONFIG["mongodb_password"]
    MONGODB_AUTH_DATABASE = CONFIG["mongodb_auth_database"]
