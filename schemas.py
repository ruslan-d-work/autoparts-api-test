from typing import Optional
from pydantic import BaseModel

class AutoPartBase(BaseModel):
    name: str
    description: str

class AutoPartCreate(AutoPartBase):
    pass

class AutoPart(AutoPartBase):
    id: int

    class Config:
        orm_mode = True

class AutoPartUpdate(BaseModel):
    name : Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
