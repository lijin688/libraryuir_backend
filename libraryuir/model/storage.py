from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import Table, Column, BOOLEAN, String, DateTime, Date
from sqlalchemy.databases import mysql
from sqlalchemy.dialects.mysql import DATE, DOUBLE, FLOAT, TIMESTAMP, TINYINT, JSON, DECIMAL
import pymysql
pymysql.install_as_MySQLdb()

from conf import settings
metadata = MetaData()

engine = create_engine(URL( **settings.DATABASE_CONFIG), connect_args={'charset': 'utf8'}, echo=True,
                        pool_recycle=1200, pool_size=400)

metadata.bind = engine
session_factory = sessionmaker(
    autocommit=False, autoflush=False,
    expire_on_commit=False, bind=engine

)

Session = scoped_session(session_factory)
Base = declarative_base()
Base.query = Session.query_property()

Integer = INTEGER = mysql.INTEGER
LongText = LONGTEXT = mysql.LONGTEXT
BigInteger = BIGINT = mysql.BIGINT
Timestamp = TIMESTAMP
VarChar = VARCHAR = mysql.VARCHAR
Char = CHAR = mysql.CHAR


class SessionMaker(object):
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        session = self.session
        if exc_type is None:
            session.commit()
        else:
            session.rollback()
        session.close()
        if exc_type != None:
            return False


class ORMBase(object):
    def __init__(self, auto_add=False, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
            if auto_add:
                self.add()

    def add(self):
        with SessionMaker() as session:
            session.add(self)

    def update(self, **kwargs):
        with SessionMaker() as session:
            ins = session.query(self.__class__).filter(getattr(self.__class__, 'id') == self.id).with_for_update(
                read=False).one()
            for key, value in kwargs.items():
                ins.__setattr__(key, value)
            session.add(ins)

    def update_add(self, **kwargs):
        with SessionMaker() as session:
            ins = session.query(self.__class__).filter(getattr(self.__class__, 'id') == self.id).with_for_update(
                read=False).one()
            for key, value in kwargs.items():
                ins.__setattr__(key, ins.__getattribute__(key) + value)
            session.add(ins)

    def delete(self):
        with SessionMaker() as session:
            session.delete(self)
            session.commit()
