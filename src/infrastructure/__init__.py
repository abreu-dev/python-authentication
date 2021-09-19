from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql+pyodbc://sa:RfAjiY5LL5@localhost:1433/authentication_python?driver=ODBC+Driver+17+for+SQL+Server",
                       echo=True)

Context = sessionmaker(bind=engine)
context = Context()

Base = declarative_base()
