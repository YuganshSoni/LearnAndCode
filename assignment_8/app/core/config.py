from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Annotated

class Settings(BaseSettings):
    LOCATION_IQ_API_KEY: Annotated[str, Field(validation_alias="LOCATION_IQ_API_KEY")]
    LOCATION_IQ_BASE_URL: Annotated[str, Field(default="https://us1.locationiq.com/v1/search")]

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
