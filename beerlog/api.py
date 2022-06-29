from fastapi import FastAPI
from beerlog.core import get_beers_from_database

api = FastAPI(title='Beerlog')


@api.get('/beers/')                     #permite utilizar os dados na api
def list_beers():                       #funçao que retorna uma lista de cervejas
    beers = get_beers_from_database()
    return beers