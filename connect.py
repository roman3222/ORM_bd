import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def connect_db(db_name, host='localhost', port=5432, user='postgres', password='password'):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    Session = sessionmaker(bind=engine)
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
    return session


