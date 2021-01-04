from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/items/{item_id}')
async def read_items(
    item_id: int = Path(..., title='The ID of the item to get', ge=1, le=1000)
):
    return {'item_id': item_id}
