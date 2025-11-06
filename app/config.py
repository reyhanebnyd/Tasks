import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    
    PROJECT_NAME = "Task Manager API"
    VERSION = "1.0.0"
    DESCRIPTION = "Simple CRUD API built with FastAPI and PostgreSQL"

    
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./tasks.db"  
    )

settings = Settings()
