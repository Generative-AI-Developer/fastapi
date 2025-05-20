from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price : int | None =None
