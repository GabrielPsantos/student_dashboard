# Hands-on - Desenvolvimento Backend

Essa aplicação gerencia o CRUD de turmas e seus alunos

### Libs Utilizadas

- Flask
- flask_sqlalchemy
- marshmallow_sqlalchemy
- flask-jwt-extended

### Construa o ambiente

    docker-compose up --b --d

### Rode as migrations

    docker-compose exec web flask db init
    docker-compose exec web flask db migrate
    docker-compose exec web flask db upgrade
  
### Testes e cobertura

    docker-compose exec web coverage run --source=project -m unittest discover -s tests/

#### Gerando relatórios de cobertura

    docker-compose exec web coverage html                                                           

### REST API

##### Execução no Postman

    Exportar arquivo "student_dashboard.postman_collection.json" no Postman e executar requisições
