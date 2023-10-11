import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
    ### Secret JWT ###
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
    MYSQL_TYPE = os.getenv("MYSQL_TYPE")
    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASS = os.getenv("MYSQL_PASS")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_DB = os.getenv("MYSQL_DB")