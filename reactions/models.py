from sqlalchemy import (
    Column,
    Index,
    Integer,
    String)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class UserApp(Base):
    __tablename__ = 'user_app'
    id = Column(Integer, primary_key=True)  # temporary
    api_key = Column(String(length=36))  # should be primary
    secret_key = Column(String(length=36))

# Index('api_key_index', UserApp.api_key, unique=True, mysql_length=36)
