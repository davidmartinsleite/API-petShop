import os
from urllib.parse import urlparse
from fastapi.testclient import TestClient
import pytest
import copy
from src.database.database_utils import get_database_uri
from src.repositorios.repositorio_pet import RepositorioPet
from sqlalchemy.engine import Engine
from src.entidades import Base, Pet
from src.database.database_utils import create_session, build_engine
from main import app


client = TestClient(app)


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
    def repo_pet(self, session):
        return RepositorioPet(session=session)

    def test_adicionar_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet(test_adicionar_pet)", idade=3, peso=9, tutor_id=1)
        pet_adicionado = repo_pet.adicionar(pet)
        print(pet)
        pet_do_banco = (session.query(Pet).filter(Pet.id == pet_adicionado.id).one())
        assert pet_adicionado == pet_do_banco
        session.query(Pet).delete()
        session.commit()

    def test_seleciona_todos_os_pets(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet(test_seleciona_todos_os_pets)", idade=3, peso=9, tutor_id=1)
        session.add(pet)
        pets = repo_pet.selecionar()
        pets_do_banco = session.query(Pet).all()
        assert pets == pets_do_banco
        session.query(Pet).delete()
        session.commit()

    def test_selecionar_apenas_um_pet(self, repo_pet, session):
        pet1 = Pet(nome_pet="nome_pet1(test_selecionar_apenas_um_pet)", idade=1, peso=11, tutor_id=1)
        session.add(pet1)
        pet2 = Pet(nome_pet="nome_pet2(test_selecionar_apenas_um_pet)", idade=7, peso=22, tutor_id=2)
        session.add(pet2)
        pet2_adicionado = session.query(Pet).filter_by(idade=7).first()
        pet_especifico = repo_pet.selecionar_especifico(pet2_adicionado.id)
        assert pet_especifico == pet2_adicionado
        session.query(Pet).delete()
        session.commit()

    def test_deletar_um_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet1(test_deletar_um_pet)", idade=1, peso=11, tutor_id=1)
        session.add(pet)
        session.commit()
        repo_pet.deletar(1)
        pets_do_banco = session.query(Pet).all()
        assert pets_do_banco == []
        session.query(Pet).delete()
        session.commit()

    def test_atualizar_pet(self, repo_pet, session):
        pet = Pet(nome_pet="nome_pet1(test_atualizar_pet)", idade=1, peso=11, tutor_id=1)
        pet_adicionado_original = copy.copy(repo_pet.adicionar(pet))
        pet_adicionado_atualizado = repo_pet.atualizar(1, nome_pet="novo nome_pet1(test_atualizar_pet)", idade=2, peso=22, tutor_id=2)
        assert pet_adicionado_original != pet_adicionado_atualizado
        session.query(Pet).delete()
        session.commit()
