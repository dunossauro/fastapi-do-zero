from contextlib import contextmanager
from pathlib import Path

from invoke import task
from rich import print
from tomllib import loads

migration_04 = """CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	email VARCHAR NOT NULL, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, updated_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username)
);
""" # noqa

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
"""  # noqa

migration_09 = migration_05 + """CREATE TABLE todos (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
	state VARCHAR(5) NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
"""  # noqa

dotenv = """DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
"""

fake_dotenv = """DATABASE_URL="sqlite:///database.db"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
"""


@contextmanager
def env_file(path: Path):
    with open(path / '.env', 'w', encoding='utf-8') as file:
        file.write(fake_dotenv)

    yield

    with open(path / '.env', 'w', encoding='utf-8') as file:
        file.write(dotenv)


@task
def test_migrations(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        database = path / 'database.db'

        if database.exists():
            database.unlink()

        with c.cd(str(path)):
            if int(path.parts[-1]) >= 9: # noqa
                c.run('poetry install')

                with env_file(path):
                    c.run('alembic upgrade head')
                    schema = c.run('sqlite3 database.db ".schema"')
                    assert schema.stdout == migration_09

            elif int(path.parts[-1]) == 4: # noqa
                c.run('poetry install')
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_04

            elif int(path.parts[-1]) >= 5: # noqa
                c.run('poetry install')
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_05


@task
def update_project(c):
    c.run('rm -rf .venv')
    toml = Path('.') / 'pyproject.toml'
    toml_tables = loads(toml.read_text())
    toml_project = toml_tables['project']
    dependencies = toml_project['dependencies']

    if (Path('.') / 'poetry.lock').exists():
        c.run('rm poetry.lock')

    for dep in sorted(dependencies):
        dep = dep.split()[0]
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
def test_act(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            if (path / '.github').exists():
                c.run('act')


@task
def test_docker_build(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            if (path / 'compose.yaml').exists():
                c.run('docker compose build')


@task
def test_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run('poetry install')
            c.run('poetry run task test')


@task
def command_sub(c, cmd):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run(cmd)


@task
def update_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')

    for path in sorted(code_path):
        toml = path / 'pyproject.toml'
        toml_tables = loads(toml.read_text())
        toml_project = toml_tables['project']
        dependencies = toml_project['dependencies']

        poetry_toml = toml_tables['tool']['poetry']
        dev_dependencies = poetry_toml['group']['dev']['dependencies']

        print(path)
        with c.cd(str(path)):
            c.run('rm -rf .venv')
            if (path / 'poetry.lock').exists():
                c.run('rm poetry.lock')

            for dep in sorted(dependencies):
                dep = dep.split()[0]
                print(dep, path)

                if dep in 'fastapi':
                    c.run('poetry add "fastapi[standard]@latest"')

                elif dep in 'pydantic':
                    c.run('poetry add "pydantic[email]@latest"')

                elif dep in'pwdlib':
                    c.run('poetry add "pwdlib[argon2]@latest"')

                elif dep in 'psycopg':
                    c.run('poetry add "psycopg[binary]@latest"')

                else:
                    c.run(f'poetry add {dep}@latest')

            for dep in dev_dependencies:
                c.run(f'poetry add --group dev {dep}@latest')

            c.run('poetry install')
