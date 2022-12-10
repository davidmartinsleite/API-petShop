from src.entidades import Tutor, Pet
from src.repositorio_tutor import RepositorioTutor
from src.reposito_pet import RepositorioPet


# isso são instancias do repositorio
repo_pet = RepositorioPet()
repo_tutor = RepositorioTutor()


# RepositorioTutor().adicionar('Afonso', 'rua lorenzo melo', '(85) 9 3366-1122')
# RepositorioTutor().adicionar('thiago', 'rua castelo branco', '(85) 9 9990-5675')
# tutor = RepositorioTutor().deletar(3)
# tutor = RepositorioTutor().selecionar()
# print(tutor)
#
# RepositorioTutor().adicionar('nome', 'endereço', '(99) 9 9999-9999')
# print(dado)


# tutor = Tutor(nome='nome', endereco='endereço', telefone='(99) 9 9999-9999')
# repo_tutor.adicionar(tutor)

pet = Pet(nome_pet="nome_pet", idade=5, peso=23, tutor_id=4)
repo_pet.adicionar(pet)

dado = repo_pet.selecionar()
print(dado)
