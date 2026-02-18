"""pydantic models for user service"""

from pydantic import BaseModel, Field


class User(BaseModel):  # pylint: disable=too-few-public-methods
    """a pydantic data model for a task, for validation"""

    # need to validate the user email (pydant function), and uuid being unique
    id: int = Field(description="unique identifier for this user UUID")
    name: str = Field(description="user's name")
    email: str = Field(description="users's email")
