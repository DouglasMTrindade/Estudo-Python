import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('IPINFO_API_KEY')