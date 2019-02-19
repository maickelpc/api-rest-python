# api-rest-python
Projeto de uma API Rest em python com Django , e Django-rest-framework

#Inicialização
Para inicializar, é necessário ter instalado o python3 ou superior e seguir os passos:
1 - Acessar a raiz do projeto
2 - Ativar o venv com o comando (em linux) ". <diretorio venv>/bin/activate".
3 - Iniciar o server, de dentro do diretorio <API> com o comando (em linux) "python3 manage.py runserver"


Para uso sem MYSQL comentar o bloco de código de configuração do mysql em api/api/settings.py e descomentar a parte do codigo para sqlite3


#Api autorizado somente por token.
Para requisitar o token, chama a URL da aplicação com o sufixo: /api-token-auth/, form-data ou x-www-form-urlencoded passando os campos username: 'login' e password: 'senha', caso de form-urlencoded, passar atributos como um Json { "username": "user", "password", "senha"}.

Para acessar as outroas rotas da api, deve passar no Header a key "Authorization", com o valor "Token + tokenrespondidonometodoacima".


#Nota:
na API Core, existem 3 formas de filtro de dados deixadas como exemplo para ser usada nos melhores momentos:

1 - Manual: Utilizada no User, definida manualmente campo a campo, e a forma de busca na queryset. neste caso, passa os parametros na querystring

2 - DjangoFilterBackend: Utilizada no Permission, Filtra os campos explicitados no item "filter_fields" da queryset de maneira exata, case sensitive. ideal para buscar por números, datas exatas ou booleanos. para isso, os fields devem ser passados na querystring

3 - SearchFilter: Utilizada no Role, para isso, basta passar na querystring a key search="dados", que ele busca em todos os fields, os dados, ou parte deles.
