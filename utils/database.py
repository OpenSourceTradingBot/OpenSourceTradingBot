import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def get_session():
    """Returns a new session."""
    return session

def close_session():
    """Closes the given session."""
    try:
        get_session().close()
    except Exception as e:
        print(f"Error closing session: {e}")
        raise

