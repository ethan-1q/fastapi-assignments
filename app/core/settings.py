
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator, AnyUrl
from pydantic.tools import lru_cache

from app.core.vault import get_vault_secrets, load_vault_secrets_from_vault_file, save_vault_secrets_to_vault_file


class MysqlDsn(AnyUrl):
    allowed_schemes = {'mysql'}
    user_required = True


class Settings(BaseSettings):
    PROJECT_NAME: str = "ethan-fastapi-assignments"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    VAULT_TOKEN: str = ''
    VAULT_ICP_DB_KEY: str = ''
    VAULT_MY_DB_KEY: str = ''

    ICP_MYSQL_USER: str = ''
    ICP_MYSQL_PASSWORD: str = ''
    ICP_MYSQL_HOST: str = ''
    ICP_MYSQL_PATH: str = ''
    ICP_DATABASE_URL: Optional[str] = None

    @validator("ICP_DATABASE_URL", pre=True)
    def assemble_icp_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        vault_key = values.get('VAULT_ICP_DB_KEY')
        vault_token = values.get('VAULT_TOKEN')

        db_info = {
            'user': values.get('ICP_MYSQL_USER'),
            'password': values.get('ICP_MYSQL_PASSWORD'),
            'host': values.get('ICP_MYSQL_HOST'),
            'path': values.get('ICP_MYSQL_PATH')
        }

        vault_data = get_vault_secrets(vault_key, vault_token)
        if vault_data:
            save_vault_secrets_to_vault_file(vault_data, vault_key)
            db_info.update(vault_data)
        else:
            vault_data = load_vault_secrets_from_vault_file(vault_key)
            if vault_data:
                db_info.update(vault_data)

        return MysqlDsn.build(
            scheme="mysql",
            user=db_info['user'],
            password=db_info['password'],
            host=db_info['host'],
            path=db_info['path']
        )

    MY_MYSQL_USER: str = ''
    MY_MYSQL_PASSWORD: str = ''
    MY_MYSQL_HOST: str = ''
    MY_MYSQL_PATH: str = ''
    MY_DATABASE_URL: Optional[str] = None

    @validator("MY_DATABASE_URL", pre=True)
    def assemble_my_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        vault_key = values.get('VAULT_MY_DB_KEY')
        vault_token = values.get('VAULT_TOKEN')

        db_info = {
            'user': values.get('MY_MYSQL_USER'),
            'password': values.get('MY_MYSQL_PASSWORD'),
            'host': values.get('MY_MYSQL_HOST'),
            'path': values.get('MY_MYSQL_PATH')
        }

        vault_data = get_vault_secrets(vault_key, vault_token)
        if vault_data:
            save_vault_secrets_to_vault_file(vault_data, vault_key)
            db_info.update(vault_data)
        else:
            vault_data = load_vault_secrets_from_vault_file(vault_key)
            if vault_data:
                db_info.update(vault_data)

        return MysqlDsn.build(
            scheme="mysql",
            user=db_info['user'],
            password=db_info['password'],
            host=db_info['host'],
            path=db_info['path']
        )

    GENERATE_SCHEMAS: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
