#!/bin/sh

# Executa as migrações do banco de dados
alembic upgrade head

# Inicia a aplicação
uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app
