from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
#os.getenv('POSTGRESQL_KEY') #like:
POSTGRESQL_DATABASE_URL = os.getenv('POSTGRESQL_KEY') #'postgresql://postgres:testpass1234!@localhost/TodoApplicationDatabase'
# MYSQL_DATABASE_URL = 'mysql+pymysql://root:testpass1234!@127.0.0.1:3306/TodoApplicationDatabase'


# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(POSTGRESQL_DATABASE_URL)
# engine = create_engine(MYSQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
