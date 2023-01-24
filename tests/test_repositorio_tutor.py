import os
from urllib.parse import urlparse
from fastapi.testclient import TestClient
import pytest
import copy
from src.database.database_utils import get_database_uri
from src.repositorios.repositorio_tutor import RepositorioTutor
from src.entidades import Base, Tutor
from src.database.database_utils import create_session, build_engine
from main import app

client = TestClient(app)
from sqlalchemy.engine import Engine


class TestRepositorioPet:
    @pytest.fixture
    def database_uri(self):
        uri = get_database_uri()
        database_path = urlparse(uri).path

        if os.path.exists(database_path) and os.path.isfile(database_path):
            os.remove(database_path)

        yield uri

        if os.path.exists(database_path) and os.path.isfile(database_path):
            os.remove(database_path)

    @pytest.fixture
    def engine(self, database_uri):
        return build_engine(database_uri)

    @pytest.fixture
    def session(self, engine):
        return create_session(engine)

    @pytest.fixture(autouse=True)
    def Base(self, engine: Engine):
        return Base.metadata.create_all(engine)

    @pytest.fixture
    def repo_tutor(self, session):
        return RepositorioTutor(session=session)

    def test_adicionar_tutor(self, repo_tutor, session):
        session.query(Tutor).delete()
        session.commit()
        tutor = Tutor(nome="nome", endereco="endereço", telefone="(99) 9 9999-9999")
        tutor_adicionado = repo_tutor.adicionar(tutor)
        tutor_do_banco = (session.query(Tutor).filter(Tutor.id == tutor_adicionado.id).one())
        assert tutor_adicionado == tutor_do_banco
        session.query(Tutor).delete()
        session.commit()

    def test_seleciona_todos_os_tutores(self, repo_tutor, session):
        tutor = Tutor(nome="nome", endereco="endereço", telefone="(99) 9 9999-9999")
        session.add(tutor)
        tutores = repo_tutor.selecionar()
        tutores_do_banco = session.query(Tutor).all()
        assert tutores == tutores_do_banco
        session.query(Tutor).delete()
        session.commit()

    def test_selecionar_apenas_um_tutor(self, repo_tutor, session):
        tutor1 = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        session.add(tutor1)
        tutor2 = Tutor(nome="nome2", endereco="endereço 2", telefone="(22) 2 2222-2222")
        tutor2_adicionado = repo_tutor.adicionar(tutor2)
        tutor_especifico = repo_tutor.selecionar_especifico(2)
        assert tutor_especifico == tutor2_adicionado
        session.query(Tutor).delete()
        session.commit()

    def test_deletar_um_tutor(self, repo_tutor, session):
        tutor = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        session.add(tutor)
        session.commit()
        repo_tutor.deletar(1)
        tutores_do_banco = session.query(Tutor).all()
        assert tutores_do_banco == []
        session.query(Tutor).delete()
        session.commit()

    def test_atualizar_tutor(self, repo_tutor, session):
        tutor = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        tutor_adicionado_original = copy.copy(repo_tutor.adicionar(tutor))
        tutor_adicionado_atualizado = repo_tutor.atualizar(1, nome="novo nome", endereco='endereço novo', telefone='(88) 8 8888-8888')
        assert tutor_adicionado_original != tutor_adicionado_atualizado
        session.query(Tutor).delete()
        session.commit()

