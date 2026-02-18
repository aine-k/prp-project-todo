"""tests for the db module of the task service"""
import os

import pytest
from app.db import get_db_session
from dotenv import load_dotenv
from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import sessionmaker

# load env variables for testing environment
load_dotenv(override=True)
DATABASE_URI = os.getenv('TEST_DATABASE_URI')


@pytest.fixture
def init_test_db():
    """initialise the database for testing"""
    engine = create_engine(
        DATABASE_URI,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine)

    with testing_session() as db_session:
        yield db_session


def test_db_exists(init_test_db):  # pylint: disable=redefined-outer-name
    """check that the db exists"""
    assert init_test_db.execute(text("SELECT 1")).scalar() == 1


def test_create_and_read(init_test_db):
    """create and read a task from the database"""
    # this might be a services test?
    # add one task and assert that it is present in the db
    assert True  # temp
