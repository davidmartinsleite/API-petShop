# API-petShop
Backend de uma aplicação para petshop, com foco na apredizagem.


## Dependências
Você precisa
- python 3 instalado 
- git instalado


## Como construir 

Essas informções são um passo-a-passo educativo, afim de auxiliar novos programadores, 
as informações foram construidas com base no windwos 10.

- Abrir o Git bash na pasta desejada, execute o sequinte programa:


    git clone https://github.com/kenomori/API-petShop.git
 
- Com a pasta clonada abra o projeto com sua IDE
- no `Terminal`  digite:


    pip install -r requerimentos.txt 



### o banco de dados

O pojeto do banco de dados é em SQlite, isso facilita a aprendisagem, 
já que requer de menos conhecimentos para o entendimento do funcionamento. 

## Como rodar a aplicação localmente

Com todas as atualizações de requerimento feitas, o programa pode ser execultado 
com um comando no `Terminal` 

    uvicorn main:app --reload


### Testes da API

Com o programa inicializado ele vai gerar o sequinte endereço para acesso: 

http://127.0.0.1:8000/docs

Caso toda a instalação estiver bem sucedida, ao acessar esse endereço ele vai abir o 
`FastAPI` com todas as funções de controle já aplicadas. 
