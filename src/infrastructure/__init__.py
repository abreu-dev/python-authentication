from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite://")

Context = sessionmaker(bind=engine)
context = Context()

Base = declarative_base()
