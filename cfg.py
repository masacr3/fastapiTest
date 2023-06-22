import os
from dotenv import load_dotenv

env_path = '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    MONGO_URI:str = os.getenv("MONGO_URI")
    MONGO_DB:str = os.getenv("MONGO_DB")
    MONGO_TABLE_MEDICACION:str = os.getenv("MONGO_TABLE_MEDICACION")


settings = Settings()