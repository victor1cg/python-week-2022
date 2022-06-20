from dataclasses import dataclass
#dateclass é utilizado para guardar dados.

#definindo os tipos consigo realizar uma validação
#@dataclass é um decorador, injetar novos metodos e classes; Cria automatica// um inicializador __init__
@dataclass
class Beer2:
    name: str
    style: str
    flavor: int
    imagem: int
    cost: int

#Criar um objeto que se pareça com um tabela
from typing import Optional             #ajuda a criar o id aleatorio
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator

class Beer(SQLModel, table = True):
    id: Optional[int] =Field(primary_key=True, default = None)     #Obrigatorio ter id para o sql
    name: str
    style: str
    flavor: int
    imagem: int
    cost: int

brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, imagem=8, cost=10)
