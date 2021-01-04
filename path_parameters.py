from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# Path Parameters
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/items/me')
async def le_item_me():
    return {'item_id': 'O item atual.'}


@app.get('/items/{item_id}')
async def le_item(item_id: int):
    return {'item_id': item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    print(model_name, model_name.value)

    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


@app.get('/files/{file_path:path}')
async def ler_arquivo(file_path: str):
    return {'file_path': file_path}
