from dataclasses import dataclass
# dateclass é utilizado para guardar dados.

# definindo os tipos consigo realizar uma validação
# @dataclass é um decorador, injetar novos metodos e classes; Cria automatica// um inicializador __init__


@dataclass
class Beer2:
    name: str
    style: str
    flavor: int
    imagem: int
    cost: int

# -------------
# Criar um objeto que se pareça com um tabela
from typing import Optional             #ajuda a criar o id aleatorio
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator          #validador, por exemplo o sabor de 1-10
from statistics import mean             #biblioteca para calcular media
from datetime import datetime

class Beer(SQLModel, table = True) :
    id: Optional[int] = Field(primary_key=True, default = None)      #Obrigatorio ter id para o sql.
    name: str                                                       #temos os atributos e os metodos
    style: str
    flavor: int
    image: int
    cost: int
    rate: int=0                                                     #adicionar o rate, com default 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor","image","cost")                             #aplicar o mesmo design pattern.DECORATOR
    def validating_ratings(cls, v, field):                          #função associada a essa classe.
        if v < 1 or v > 10:
            raise RuntimeError(f'\n{field.name} must be between one and ten')
        return v

    @validator ('rate',always = True)
    def calculate_rate(cls,v,values):
        rate = mean(
            [values['flavor'],values['image'],values['cost']]
            )
        return int(rate)


brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, image=8, cost=10)