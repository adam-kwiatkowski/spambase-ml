from pydantic import BaseModel


class Email(BaseModel):
    text: str
