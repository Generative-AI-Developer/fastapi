from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
 return "Hello Asif"


@app.get("/items")
def greet(q:int = 0, skip:int = 10):
 return ("Q", q, "Skip", skip)