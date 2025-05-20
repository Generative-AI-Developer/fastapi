from fastapi import FastAPI, Body
from models import Item

app = FastAPI()

@app.post("/items")
async def read_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

@app.post("/items/item")
async def update_item_1(item: str = Body(embed=True)):
    return item