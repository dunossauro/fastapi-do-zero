FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY . .

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8888
CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8888", "fast_zero.app:app" ]
