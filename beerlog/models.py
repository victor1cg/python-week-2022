from dateclasses import dataclass
#dateclass é utilizado para guardar dados.

#definindo os tipos consigo realizar uma validação
#@dataclass é um decorador, injetar novos metodos e classes; Cria automatica// um inicializador __init__
@dataclass
class Beer:
    name: str
    style: str
    flavor: int
    imagem: int
    cost: int

brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, imagem=8, cost=10)
