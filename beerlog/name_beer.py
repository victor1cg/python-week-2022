from sqlmodel import select
from beerlog.database import engine
from beerlog.models import Beer

with Session(engine) as session:
    beers = select(Beer)
    results = session.exec(sql)
    for beer in results:
        print(beer.name)
