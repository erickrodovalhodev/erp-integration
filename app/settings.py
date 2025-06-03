from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    erp_url: str
    erp_token: str
    hmac_secret: str
    database_url: str
    timeout: float = 10.0

    model_config = {"env_prefix": "ERP_"}


settings = Settings()