import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+pymysql://root:123@127.0.0.1/macondo')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    lastname = sqlalchemy.Column(sqlalchemy.String(50))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

u = User(name='seba')

session.add(u)
session.commit()
