from dataclasses import dataclass

# dateclass é utilizado para guardar dados.

# definindo os tipos consigo realizar uma validação
# @dataclass é um decorador, injetar novos metodos e classes; Cria automatica// um inicializador __init__ > com isso não precisa criar o inicializador
# vai modificar e injetar novas funções,


@dataclass
class Beer2:
    name: str  # anotação de tipos é python moderno, como são dados externos a validação é importante
    style: str
    flavor: int
    image: int
    cost: int


# criando um objeto e armazenado dados
skol = Beer2(name="Skol", style="Pilsen", flavor=4, image=10, cost=10)

# -------------
# A dataclass é padrão, porem SQLMODEL é muito melhor para atrelar dados;
# Criar um objeto que se pareça com um tabela;
from typing import Optional  # ajuda a criar o id aleatorio
from sqlmodel import SQLModel, Field
from sqlmodel import select  # SQLModel = Junção do SQLAlchemy + Pydantic
from pydantic import validator  # validador, por exemplo o sabor de 1-10
from statistics import mean  # biblioteca para calcular media
from datetime import datetime


class Beer(
    SQLModel, table=True
):  # Pelo fato de ser SQLModel, é possivel criar tabelas SQL
    id: Optional[int] = Field(
        primary_key=True, default=None
    )  # Obrigatorio ter id para o sql.
    name: str  # temos os atributos e os metodos
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0  # adicionar o rate, com default 0
    date: datetime = Field(default_factory=datetime.now)

    @validator(
        "flavor", "image", "cost"
    )  # DECORATOR - função associada a classe, é metodo.
    def validating_ratings(
        cls, v, field
    ):  # cls - classe, v - valor a ser validado, field - campo a ser validado
        if v < 1 or v > 10:  # função associada a essa classe.
            raise RuntimeError(
                f"\n{field.name.upper()} must be between one and ten!"
            )
        return v

    @validator(
        "rate", always=True
    )  # @validator vai acionar e retornar a função
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=10)
