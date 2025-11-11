import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN_API = os.getenv('TOKEN_API')
