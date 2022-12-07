from tutor_comandos import RepositorioTutor

RepositorioTutor().adicionar('Afonso', 'rua lorenzo melo', '(85) 9 3366-1122')


RepositorioTutor().adicionar('thiago', 'rua castelo branco', '(85) 9 9990-5675')
tutor = RepositorioTutor().deletar(3)
tutor = RepositorioTutor().selecionar()
print(tutor)
