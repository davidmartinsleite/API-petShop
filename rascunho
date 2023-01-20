import os
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.entidades import Base

CURRENT_DIR = os.getcwd()


def build_engine(url: Optional[str] = None):
    url = url or f"sqlite:///{CURRENT_DIR}/petshop.db"
    print(url)
    engine = create_engine(url=url)
    return engine


def create_session(engine=None):
    engine = engine or build_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_database():
    engine = build_engine()
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()

# Estamos criando uma instância de Engine com o sqlite
# Podemos agora gerar toda a estrutura do banco usando um método
# utilitário da classe Base que criamos.
