import os
import sys
import time
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy import Column, Integer, Unicode, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils.functions import database_exists
from sqlalchemy import exc


Base = declarative_base()


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    articles = relationship("Article", backref="sources")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(Unicode, unique=True, nullable=False)

    published = Column(Date)
    title = Column(Unicode)
    body = Column(Unicode)

    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    source = relationship("Source")


def seed():
    eng = engine()
    Base.metadata.create_all(eng)


def session():
    eng = engine()
    return sessionmaker(eng)


def engine():
    database_name = os.environ["DATABASE_NAME"]
    database_user = os.environ["DATABASE_USER"]
    database_password = os.environ["DATABASE_PASSWORD"]

    db_url = 'postgresql://%s:%s@storage:5432/%s' % (
        database_user,
        database_password,
        database_name
    )

    max_tries = 10
    wait_increment = 3  # in seconds
    engine = None
    for n in range(1, max_tries+1):
        try:
            if database_exists(db_url):
                engine = create_engine(db_url, echo=True, echo_pool=True)
        except:
            pass

        if engine is None:
            if n == max_tries:
                raise Exception("could not connect to database")

            wait_time = n * wait_increment
            print("Could not connect to database, attempt %d/%d" % (n, max_tries) +
                  "\nWaiting for %d seconds to reattempt" % wait_time)
            sys.stdout.flush()
            time.sleep(n * wait_increment)
        else:
            return engine
