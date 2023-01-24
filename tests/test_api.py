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

"""
1. quando apertar o botao esquerdo, deve acender a luz verde
2. quando apertar o botao direito, deve acender a luz vermelha
3. quando apertar os dois botoes ao mesmo tempo e segurar, deve piscar as duas luzes
4. quando apertar os dois botoes ao mesmo tempo, rapidamente, nada deve acontecer
5. quando apertar os dois botoes de forma intermitente, entre esquerdo e direito, nada deve acontecer.
6. quando apertar os dois botoes, ao mesmo tempo, de forma rapida e intermitente, nada deve acontecer. 
"""

"""
# PARA CADA TESTE
1. Faço o setup do ambiente: subir infra estrutura necessaria
2. Criar objetos auxiliares o que eu preciso para testar algo
3. Realizar o teste
4. Limpar os objetos auxiliares e infraestrutura
"""
client = TestClient(app)


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

    def teste_adicionar_tutor_pela_api(self, repo_tutor: RepositorioTutor):
        tutor = Tutor(nome="nome(teste_tutor)", endereco="endereço", telefone="(99) 9 9999-9999")
        repo_tutor.adicionar(tutor)
        resposta = client.get("/tutores/seleciona")
        conteudo = resposta.json()
        assert resposta.status_code == 200

    #
    # def test_ver_todos_os_tutores(self, repo_tutor: RepositorioTutor):
    #
    #     tutor1 = Tutor(nome="nome1", endereco="endereço1", telefone="(99) 9 9999-9999")
    #     tutor2 = Tutor(nome="nome2", endereco="endereço2", telefone="(99) 9 9999-8888")
    #     repo_tutor.adicionar(tutor1)
    #     repo_tutor.adicionar(tutor2)
    #
    #     resposta = client.get("/tutores/seleciona")
    #     conteudo = resposta.json()
    #     assert resposta.status_code == 200
    #     assert len(conteudo) == 2
    #
    # def test_criar_novo_tutor(self):
    #     resposta = client.post(
    #         "/tutores/adcionar",
    #         json={"nome": "Joao", "endereco": "Rua 2", "telefone": "88 9 9933-1122"},
    #         # json={"nome": "nome"},
    #     )
    #
    #     # assert resposta.status_code == 200
