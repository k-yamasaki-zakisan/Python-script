from typing import Optional, List
from enum import Enum

from fastapi import FastAPI, Cookie, Query, Header
from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    alexnet_message = "Deep Learning FTW!"
    resnet_message = "LeCNN all the images"
    lenet_message = "Have some residuals"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hell World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}

@app.get("/user/me")
async def read_user_me():
    return {"user_id":"the current user"}

@app.get("/user/{user_id}")
async def read_user_me(user_id:int):
    return {"user_id":user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message":ModelName.alexnet_message }
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message":ModelName.resnet_message }
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message":ModelName.lenet_message }

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result

# リクエストバリデーション追加
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query("fixedquery", min_length=3, max_length=50),
    user_agent: Optional[List[str]] = Header(None)
): # デフォルト値、バリデーション*2
    results = {
        "items": [{"item_id":"Foo"}, {"item_id": "Bar"}],
        "X-Token values": x_token
    }
    if q:
        results.update({"q": q})
    return results

@app.get("/items/cookie")
async def read_items_cookie(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}

