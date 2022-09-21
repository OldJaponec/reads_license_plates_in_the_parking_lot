from dotenv import load_dotenv

from pathlib import Path
import os

# specify the path to the .env file 
# where the environment variables are stored
dotenv_path = '.env'

# load variables
load_dotenv(dotenv_path)

# assign variables
api_key = os.environ.get('API_KEY')
database_name=os.environ.get('MONGO_DATABASE_NAME')
collection_name=os.environ.get('MONGO_DATABASE_COLLECTION_NAME')
password = os.environ.get('MONGO_USER_PASSWORD')
connection_string = os.environ.get('MONGO_CONNECTION_STRING')