from loguru import logger

from constants.setup_logs import LOGS_FILE_NAME


logger.add(LOGS_FILE_NAME)

