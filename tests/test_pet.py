import copy
import pytest
from src.repositorios.repositorio_pet import RepositorioPet
from src.entidades import Tutor, Pet
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
    def repo_pet(self, session):
        return RepositorioPet(session=session)

    @pytest.fixture(autouse=True)
    def Base(self, engine):
        Base.metadata.create_all(engine)

    def test_adicionar_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet", idade=3, peso=9, tutor_id=1)
        pet_adicionado = repo_pet.adicionar(pet)
        print(pet)
        pet_do_banco = (
            session.query(Pet).filter(Pet.id == pet_adicionado.id).one()
        )
        assert pet_adicionado == pet_do_banco

    def test_seleciona_todos_os_pets(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet", idade=3, peso=9, tutor_id=1)
        session.add(pet)
        pets = repo_pet.selecionar()
        pets_do_banco = session.query(Pet).all()
        assert pets == pets_do_banco

    def test_selecionar_apenas_um_pet(self, repo_pet, session):
        pet1 = Pet(nome_pet="nome_pet1", idade=1, peso=11, tutor_id=1)
        session.add(pet1)
        pet2 = Pet(nome_pet="nome_pet2", idade=2, peso=22, tutor_id=2)
        pet2_adicionado = repo_pet.adicionar(pet2)
        pet_especifico = repo_pet.selecionar_especifico(2)
        assert pet_especifico == pet2_adicionado

    def test_deletar_um_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet1", idade=1, peso=11, tutor_id=1)
        session.add(pet)
        session.commit()
        repo_pet.deletar(1)
        pets_do_banco = session.query(Pet).all()
        assert pets_do_banco == []

    def test_atualizar_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet1", idade=1, peso=11, tutor_id=1)
        pet_adicionado_original = copy.copy(repo_pet.adicionar(pet))
        pet_adicionado_atualizado = repo_pet.atualizar(1, nome_pet="novo nome_pet1", idade=2, peso=22, tutor_id=2)
        assert pet_adicionado_original != pet_adicionado_atualizado
