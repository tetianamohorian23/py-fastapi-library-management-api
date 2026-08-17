from datetime import date
from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str
    bio: str | None = None


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str
    summary: str | None = None
    publication_date: date | None = None


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)
