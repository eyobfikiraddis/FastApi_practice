from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"FastAPI is workinghkhh"}


@app.get("/{id}")
def get_item(id):
    return {"item_id": id}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"message": "I received your item!", "name": item.name, "price": item.price}


# if __name__ == "__main__":
#     uvicorn.run(app,host = "127.0.0.1", port = 9000)