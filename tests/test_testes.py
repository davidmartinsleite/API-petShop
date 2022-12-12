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

    def test_seleciona_todos_os_tutores(self, repo_tutor, session):
        tutor = Tutor(nome="nome", endereco="endereço", telefone="(99) 9 9999-9999")
        session.add(tutor)
        tutores = repo_tutor.selecionar()
        tutores_do_banco = session.query(Tutor).all()
        assert tutores == tutores_do_banco

    def test_selecionar_apenas_um_tutor(self, repo_tutor, session):
        tutor1 = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        session.add(tutor1)
        tutor2 = Tutor(nome="nome2", endereco="endereço 2", telefone="(22) 2 2222-2222")
        tutor2_adicionado = repo_tutor.adicionar(tutor2)
        tutor_especifico = repo_tutor.selecionar_especifico(2)
        assert tutor_especifico == tutor2_adicionado

    def test_deletar_um_tutor(self, repo_tutor, session):
        tutor1 = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        session.add(tutor1)
        session.commit()
        repo_tutor.deletar(1)
        tutores_do_banco = session.query(Tutor).all()
        assert tutores_do_banco == []

    def test_atualizar_tutor(self, repo_tutor, session):
        tutor = Tutor(nome="nome1", endereco="endereço 1", telefone="(11) 1 1111-1111")
        tutor_adicionado_original = repo_tutor.adicionar(tutor)
        tutor_adicionado_atualizado = repo_tutor.atualizar(1, 'endereço novo', '(88) 8 8888-8888')
        assert tutor_adicionado_original != tutor_adicionado_atualizado
