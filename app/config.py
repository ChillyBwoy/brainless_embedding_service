from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    allow_credentials: bool = True
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    openapi_url: str | None = None

    api_key: str = ""

    hf_token: str = ""

    embedding_model: str = ""
    embedding_cache_folder: str = ""

    vertex_ai_model: str = ""
    vertex_ai_api_key: str = ""
    vertex_ai_project_id: str = ""
    vertex_ai_location: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def __hash__(self) -> int:
        return hash(
            (
                self.debug,
                self.allow_credentials,
                "|".join(self.allow_origins),
                "|".join(self.allow_methods),
                "|".join(self.allow_headers),
                self.openapi_url,
                self.api_key,
                self.hf_token,
                self.embedding_model,
                self.embedding_cache_folder,
                self.vertex_ai_api_key,
                self.vertex_ai_project_id,
                self.vertex_ai_location,
            )
        )
