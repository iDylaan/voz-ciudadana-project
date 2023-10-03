import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
    ### Secret JWT ###
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")