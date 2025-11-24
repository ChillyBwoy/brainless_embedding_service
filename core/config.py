from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    openapi_url: str | None = None
    hf_token: str = ""
    embedding_model_name: str = ""
    prediction_model_name: str = ""
    cache_folder: str = ""

    allow_credentials: bool = True
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env")


def get_settings() -> Settings:
    return Settings()
