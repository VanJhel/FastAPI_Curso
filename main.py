from random import randint
from typing import Union
from fastapi import FastAPI

#Creación de una aplicacion FatAPI:

app = FastAPI()


@app.get('/challenge/{numero}')
def randomId(numero: int):
    return {'Respuesta': numero * 2022 + randint(1,10)}