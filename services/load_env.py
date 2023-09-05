from constants.load_env import ENV_FILE_ENCODING, ENV_FILE_NAME
from pydantic_settings import BaseSettings, SettingsConfigDict


class _EnvVar(BaseSettings):
    """
        Класс описывающий загрузку переенных окружения
    """
    model_config = SettingsConfigDict(env_file=ENV_FILE_NAME, 
                                      env_file_encoding=ENV_FILE_ENCODING)

    SECRET_KEY: str

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str


EnvVar = _EnvVar()

