# DESAFIO SIGMA - PLENO
Este projeto é uma aplicação web responsável por realizar um CRUD de produtos construída com Flask, que se conecta a um banco de dados MySQL.
## Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração
1. Clone e acesse o repositório da aplicação.
```bash
git clone https://github.com/opugacodez/sigma-pleno.git
cd sigma-pleno
```
2. Em seguida copie as variáveis de ambiente de `env.example`:
```bash
cp env.example .env
```
3. No arquivo `.env` defina o valor de `SECRET_KEY` manualmente.

## Executando a Aplicação
1. Inicie os containers
```bash
docker-compose up --build
```
-   Isso irá construir as imagens e iniciar os containers.
2. Acesse a aplicação
Após os containers estarem rodando, você pode acessar a aplicação no navegador em http://localhost:5000.

## Licença
Copyright © 2024 / Richard Barros

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste repositório, sem restrição nos direitos de usar, copiar, modificar e mesclar.