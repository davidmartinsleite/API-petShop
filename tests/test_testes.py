from repositorio_tutor import RepositorioTutor


def test_adicionar_tutor():

    assert RepositorioTutor.adicionar(0, 'nome', 'endereço', '(99) 9 9999-9999')


