from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    port: int = 8080

    openapi_url: str | None = None
    hf_token: str = ""
    model_name: str = ""
    cache_folder: str = ""

    allow_credentials: bool = True
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env")

    def __hash__(self) -> int:
        return hash(
            (
                self.debug,
                self.port,
                self.openapi_url,
                self.hf_token,
                self.model_name,
                self.cache_folder,
                self.allow_credentials,
                "|".join(self.allow_origins),
                "|".join(self.allow_methods),
                "|".join(self.allow_headers),
            )
        )
