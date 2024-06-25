from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from expenseTracker.logger import logger
import urllib.parse

load_dotenv()

def getPostgresConnection():
    try:
        # Define the PostgreSQL database URL
        DB_URL = f'postgresql://{os.getenv('DB_USER')}:{urllib.parse.quote(os.getenv('DB_PASS'))}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
        # Create an engine
        engine = create_engine(DB_URL)
        # Create a sessionmaker
        Session = sessionmaker(bind=engine)
        # Create a session
        session = Session()
        # Logging session
        logger.info(f'Postgresql session created! Session object: {session}')
        return session
    except Exception as exc:
        logger.exception(f'Exception occured in getPostgresConnection(): {exc}')
        raise Exception(exc)
