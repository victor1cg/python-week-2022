"""from .config import settings
import sys


def main():
    # print("Hello from", settings.NAME)    #esse aqui veio default
    print(sys.argv[1:])      """  # esse aqui traz as infos do add

import typer
from typing import Optional
from beerlog.core import *
from rich.table import Table               #escrever texto formatado no terminal
from rich.console import Console            

main = typer.Typer(help="Beer Management Application")  # Nome da aplicação
console = Console()

# Funções do typer
@main.command("add")  # cria o comando, typer.option passo com --
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer into database"""  # msg do help
    if add_beer_todatabase(name, style, flavor, image, cost):
        print('\nBeer added to DB!')
    else:
        print('\nNo beer inserted, Sorry!')


@main.command("list")  # mais um comando de listar breja
def list_beers(style: Optional[str]= None):
    """Lists a beers in database"""             # msg do help
    beers = get_beers_from_database()           #objeto que tem as cervejas
    table = Table(title='Beerlog')
    headers = ['id','name','style','rate','date']
    
    #criar a tabela
    for header in headers:
        table.add_column(header, style='magenta')
    
    #adicionar as linhas na tabela
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)