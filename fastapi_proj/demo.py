from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
 return "Hello Asif"


@app.get("/items")
def greet(q:int = 0, skip:int = 10):
 return ("Q", q, "Skip", skip)




fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]