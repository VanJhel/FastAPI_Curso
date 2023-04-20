from typing import Union
from fastapi import FastAPI

#Creación de una aplicacion FatAPI:

app = FastAPI()

#@app.get('/')
#def read_root():
#    return {'Hello': 'World!'}

#@app.get('/items/{item_id}')
#def read_item(item_id: int, q:Union[str, None] = None):
#    return {'item_id': item_id, 'q': q}

@app.get('/challenge/{numero}')
def randomId(numero: int):
    return {'Respuesta': numero * 2022 }
    #return {'Respuesta': numero * 2022 + random.randint(1,10)}