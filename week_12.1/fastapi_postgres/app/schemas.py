from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    name: str
    age: int
    in_active: bool

    class Config:
        from_attributes = True