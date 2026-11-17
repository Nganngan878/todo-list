from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    app_name : str = 'todo-API'
    app_namev : str = 'development'
    debug : bool = True
    database_url: str
    model_config = SettingsConfigDict(
        env_file= '.env',env_file_encoding='utf-8',extra='ignore'
    
    )


@lru_cache
def get_setting() -> Setting:
    return Setting()
