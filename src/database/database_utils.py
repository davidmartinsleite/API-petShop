import os
from typing import Optional
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.entidades import Base

CURRENT_DIR = os.getcwd()

# Função que cria uma instância de Engine, que é usada para se comunicar com o banco de dados
# Aceita um argumento opcional "url" para conectar a um banco de dados específico, se nenhuma for fornecida
# é usada uma url padrão com o diretório atual e o nome do banco de dados.


def get_database_uri() -> str | None:

    url = None
    environment = os.getenv("ENVIRONMENT", None)

    if environment == "DEV":
        url = f"sqlite:///{CURRENT_DIR}/petshop.db"

    if environment == "PROD":
        url = ""

    if not url:
        url = f"sqlite:///{CURRENT_DIR}/petshot-test-database.db"

    return url


def build_engine(database_uri: Optional[str] = None):
    uri = database_uri or get_database_uri()
    engine = create_engine(url=uri)
    return engine


# Função que cria uma sessão com o banco de dados. Aceita um argumento opcional "engine"
# para usar uma instância específica de engine, se nenhuma for fornecida é criada uma nova.
def create_session(engine=None):
    orm_engine = engine or build_engine()
    Session = sessionmaker(bind=orm_engine)
    session = Session()
    return session


# Função que cria tabelas no banco de dados usando a classe Base.
def create_database():
    engine = build_engine()
    Base.metadata.create_all(engine)


# Se o script for executado como principal, chama a função create_database
if __name__ == "__main__":
    create_database()


# Estamos criando uma instância de Engine com o sqlite
# Podemos agora gerar toda a estrutura do banco usando um método
# utilitário da classe Base que criamos.
