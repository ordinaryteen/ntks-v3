from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  PROJECT_NAME: str = "Natakos engine v3"
  DATABASE_URL: str 
  APP_SECRET: str
  DEEPSEEK_API_KEY: str  

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings() 