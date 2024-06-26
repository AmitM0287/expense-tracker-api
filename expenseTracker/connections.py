import os
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connections:
    ''' This is used to get connections ref '''
    @staticmethod
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
            # Return session
            return session
        except Exception as exc:
            raise Exception(exc)

