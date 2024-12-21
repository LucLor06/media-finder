import os
from dotenv import load_dotenv, find_dotenv

path = find_dotenv()

load_dotenv(path)

DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')