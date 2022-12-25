from typing import Union, Set, List
from fastapi import FastAPI, Query
from pydantic import BaseModel, HttpUrl, Field

app = FastAPI()

@app.get('/users/{user_id}/items/{item_id}')
async def read_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str = Field(example="Foo")
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None

@app.post("/items/")
async def create_item(item: Item):
    return Item