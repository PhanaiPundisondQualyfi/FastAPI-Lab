from pydantic import BaseModel, Field

class ItemRequest(BaseModel): # Use Field for specifics e.g., str = Field(min_length=1)
    name: str
    description: str
    price: float
    tax: float 

class ItemCreate(ItemRequest):
    pass

class ItemWithID(ItemRequest):
    id: int
