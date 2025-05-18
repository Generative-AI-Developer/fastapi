from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def greet():
 return "Hello? World?"

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id} 


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/{product}/items/{item_id}")
def get_item1(item_id: int, product: str):
    return {"item_id": item_id, "product": product} 