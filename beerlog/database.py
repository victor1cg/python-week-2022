#SqLite
from sqlmodel import create_engine                  #cria um objeto capaz de se conectar com um DB
from beerlog.config import settings 
from beerlog import models                          #tabela da classe beer seja criada    


engine = create_engine(settings.database.url)       #engine conecta ao db de arquivos

models.SQLModel.metadata.create_all(engine)         #cria a tabela do banco de dados