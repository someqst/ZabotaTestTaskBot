from pathlib import Path
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


BASE_PATH = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    OPENAI_TOKEN: SecretStr
    BOT_TOKEN: SecretStr

    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: SecretStr

    POSTGRES_HOST: str = "postgres"

    model_config = SettingsConfigDict(
        env_file=BASE_PATH / ".env", env_file_encoding="utf-8"
    )

    @property
    def DB_URL(self):
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER.get_secret_value()}:"
            f"{self.POSTGRES_PASSWORD.get_secret_value()}"
            f"@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB.get_secret_value()}"
        )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
