import pytest
from src.repositorios.repositorio_tutor import RepositorioTutor
from src.entidades import Tutor
from src.database.database_utils import create_session, build_engine
from src.entidades import Base


class TestRepositorioTutor:
    @pytest.fixture
    def engine(self):
        return build_engine("sqlite://")

    @pytest.fixture
    def session(self, engine):
        return create_session(engine)

    @pytest.fixture
    def repo_tutor(self, session):
        return RepositorioTutor(session=session)

    @pytest.fixture(autouse=True)
    def Base(self, engine):
        Base.metadata.create_all(engine)

    def test_adicionar_tutor(self, repo_tutor, session):
        tutor = Tutor(nome="nome", endereco="endereço", telefone="(99) 9 9999-9999")
        tutor_adicionado = repo_tutor.adicionar(tutor)
        tutor_do_banco = (
            session.query(Tutor).filter(Tutor.id == tutor_adicionado.id).one()
        )
        assert tutor_adicionado == tutor_do_banco

    def test_seleciona_especifico(self, repo_tutor, session):
        ...
