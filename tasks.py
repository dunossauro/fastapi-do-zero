from invoke import task
from rich import print
from pathlib import Path
from tomllib import loads

migration_05 = """CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	email VARCHAR NOT NULL, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username)
);
"""

# WIP: Ajustar o esperado dessa migração no código
migration_09 = """CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	email VARCHAR NOT NULL, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username)
);
"""


@task
def update_project(c):
    c.run('rm -rf .venv')
    toml = Path('.') / 'pyproject.toml'
    toml_tables = loads(toml.read_text())
    poetry_toml = toml_tables['tool']['poetry']
    dependencies = poetry_toml['dependencies']

    if (Path('.') / 'poetry.lock').exists():
        c.run('rm poetry.lock')

    for dep in sorted(dependencies):
        if dep == 'python':
            ...

        else:
            c.run(f'poetry add {dep}@latest')


@task
def typos_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run('poetry run typos .')


@task
def lint_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run('poetry run task lint')


@task
def test_docker_build(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            if (path / 'docker-compose.yml').exists():
                c.run('docker compose build')


@task
def test_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run('poetry install')
            c.run('poetry run task test')

            if int(path.parts[-1]) >= 5:
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_05

            elif int(path.parts[-1]) >= 9:
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_09

@task
def update_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')

    for path in sorted(code_path):
        toml = path / 'pyproject.toml'
        toml_tables = loads(toml.read_text())
        poetry_toml = toml_tables['tool']['poetry']
        dependencies = poetry_toml['dependencies']
        dev_dependencies = poetry_toml['group']['dev']['dependencies']

        print(path)
        with c.cd(str(path)):
            c.run('poetry update')
            c.run('rm -rf .venv')
            if (path / 'poetry.lock').exists():
                c.run('rm poetry.lock')

            for dep in sorted(dependencies):
                print(dep, path)
                if dep == 'pydantic':
                    c.run('poetry add "pydantic[email]@latest"')

                elif dep == 'passlib':
                    c.run('poetry add "passlib[bcrypt]@latest"')

                elif dep == 'psycopg':
                    c.run('poetry add "psycopg[binary]@latest"')

                elif dep == 'python':
                    ...

                else:
                    c.run(f'poetry add {dep}@latest')

            for dep in dev_dependencies:
                c.run(f'poetry add --group dev {dep}@latest')
