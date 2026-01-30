"""Test db config, in-mem Sqlite"""
# use an in memory sqlite database for testing
TEST_DATABASE_URI = "sqlite:///:memory:"
# requirements are for a postgres db - fix later
SQLALCHEMY_DATABASE_URI = "sqlite:///./tasks.db"
