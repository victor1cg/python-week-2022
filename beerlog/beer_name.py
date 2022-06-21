from sqlmodel import select
from database import engine
from models import Beer
from sqlmodel import Session

with beerlog.Session(engine) as session:
    beers = select(Beer)
    results = session.exec(sql)
    for beer in results:
            print(beer.name)