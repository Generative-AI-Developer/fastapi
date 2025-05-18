from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def greet():
 return "Hello? World?"

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id} 