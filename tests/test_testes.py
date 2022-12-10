from sqlalchemy import create_engine

from src.repositorio_tutor import RepositorioTutor
from sqlalchemy.orm import sessionmaker
from database.database_utils import Tutor

# engine = create_engine("sqlite:///petshop.db")

repo_tutor = RepositorioTutor()

# Session = sessionmaker(bind=engine)
# session = Session()


def test_adicionar_tutor():
    tutor = Tutor(nome="nome", endereco="endereço", telefone="(99) 9 9999-9999")
    tutor_adicionado = repo_tutor.adicionar(tutor)
    tutor_do_banco = session.query(Tutor).filter(Tutor.id == tutor_adicionado.id)
    # assert tutor_adicionado.id == tutor_do_banco.id
    # assert tutor_adicionado.nome == tutor_do_banco.nome
