#!/bin/sh

poetry run alembic upgrade head

# Perguntar a entendedores!
poetry run uvicorn --host 0.0.0.0 --port 8888 fast_zero.app:app
