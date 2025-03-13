from typing import Union
from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "SRC")))
from SRC.controller.stream_controller.stream_controller import router as stream_router

app = FastAPI()

app.include_router(stream_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
