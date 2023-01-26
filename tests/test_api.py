import os
from urllib.parse import urlparse
from fastapi.testclient import TestClient
import pytest
from sqlalchemy.engine import Engine
from src.database.database_utils import build_engine, create_session, get_database_uri
from src.repositorios.repositorio_pet import RepositorioPet
from src.repositorios.repositorio_tutor import RepositorioTutor
from src.entidades import Base, Tutor
from main import app

client = TestClient(app)


tutor01 = {
    'nome': "nome",
    'endereco': "endereço",
    'telefone': "9933556677"
}


class TestAPI:
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

    @pytest.fixture
    def repo_pet(self, session):
        return RepositorioPet(session=session)

    def test_ler_raiz(self):
        resposta = client.get("/")
        assert resposta.status_code == 200
        assert resposta.json() == {"msg": "API Petshop"}

    def test_criar_novo_tutor(self, session):
        session.query(Tutor).delete()
        session.commit()
        resposta = client.post("/tutores/adcionar/", json=tutor01)
        assert resposta.status_code == 200

    def teste_obtem_todos_os_tutores_pela_api(self, repo_tutor: RepositorioTutor, session):
        session.query(Tutor).delete()
        session.commit()
        tutor = Tutor(nome="nome1(teste_tutor)", endereco="endereço", telefone="(99) 9 9999-9999")
        repo_tutor.adicionar(tutor)
        tutor = Tutor(nome="nome2(teste_tutor)", endereco="endereço", telefone="(99) 9 9999-9999")
        repo_tutor.adicionar(tutor)
        session.commit()
        resposta = client.get("/tutores/seleciona/")
        conteudo = resposta.json()
        assert resposta.status_code == 200
        assert len(conteudo) == 2
