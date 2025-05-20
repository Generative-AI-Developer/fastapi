from fastapi import FastAPI
from models import Item

app = FastAPI()

@app.post("/items")
async def read_item(item: Item):
    return item

