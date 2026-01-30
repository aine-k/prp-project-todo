"""tests for the db module of the task service"""
import pytest
from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import declarative_base, sessionmaker


@pytest.fixture
def init_test_db():
    """initialise the database for testing"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session = sessionmaker(bind=engine)
    declarative_base().metadata.create_all(bind=engine)
    session = testing_session()
    yield session
    session.close()


def test_db_exists(init_test_db):  # pylint: disable=redefined-outer-name
    """check that the db exists"""
    assert init_test_db.execute(text("SELECT 1")).scalar() == 1
