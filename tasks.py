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
"""   # noqa

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

migration_10 = (
    migration_05
    + """CREATE TABLE todos (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
	state VARCHAR(5) NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
"""
)  # noqa

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

fake_dotenv_async = """DATABASE_URL="sqlite+aiosqlite:///database.db"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
"""


def iter_class_paths():
    base = Path('./codigo_das_aulas').resolve()
    return sorted([p for p in base.glob('*') if p.is_dir()])


def clean_venv_lock(c, path: Path):
    venv = path / '.venv'
    lock = path / 'poetry.lock'

    if venv.exists():
        c.run('rm -rf .venv')

    if lock.exists():
        lock.unlink()


@contextmanager
def env_file(path: Path, sync=True):
    with open(path / '.env', 'w', encoding='utf-8') as file:
        if sync:
            file.write(fake_dotenv)
        else:
            file.write(fake_dotenv_async)

    yield

    with open(path / '.env', 'w', encoding='utf-8') as file:
        if sync:
            file.write(fake_dotenv)
        else:
            file.write(fake_dotenv_async)


@task
def test_migrations(c):
    for path in iter_class_paths():
        print('test_migrations: ', path)
        database = path / 'database.db'

        if database.exists():
            database.unlink()

        with c.cd(str(path)):
            if int(path.parts[-1]) >= 10:   # noqa
                c.run('poetry install')

                with env_file(path, sync=False):
                    c.run('alembic upgrade head')
                    schema = c.run('sqlite3 database.db ".schema"')
                    assert schema.stdout == migration_10

            elif int(path.parts[-1]) == 4:   # noqa
                c.run('poetry install')
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_04

            elif int(path.parts[-1]) >= 5:   # noqa
                c.run('poetry install')
                c.run('alembic upgrade head')
                schema = c.run('sqlite3 database.db ".schema"')
                assert schema.stdout == migration_05


@task
def update_project(c):
    root = Path('.')
    clean_venv_lock(c, root)

    toml = root / 'pyproject.toml'

    toml_tables = loads(toml.read_text())

    toml_project = toml_tables['project']
    dependencies = toml_project['dependencies']
    dev_dependencies = toml_tables['dependency-groups']['dev']

    for dep in sorted(dependencies):
        if not '(==' in dep:
            dep = dep.split()[0]
            c.run(f'poetry add {dep}@latest')

    for dep in sorted(dev_dependencies):
        if not '(==' in dep:
            dep = dep.split()[0]
            c.run(f'poetry add --group dev {dep}@latest')


@task
def typos_sub(c):
    for path in iter_class_paths():
        print('typos_sub: ', path)
        with c.cd(str(path)):
            c.run('poetry run typos .')


@task
def lint_sub(c):
    for path in iter_class_paths():
        print('lint_sub: ', path)
        with c.cd(str(path)):
            c.run('poetry run task lint')


@task
def test_act(c):
    for path in iter_class_paths():
        github = path / '.github'
        if github.exists():
            print('test_act:', path)
            with c.cd(str(path)):
                c.run('act')


@task
def test_docker_build(c, python_version='3.12'):
    for path in iter_class_paths():
        print('test_docker_build:', path)
        dockerfile = path / 'Dockerfile'

        with c.cd(str(path)):
            if dockerfile.exists():
                text = dockerfile.read_text()
                text = text.replace(
                    'FROM python:', f'FROM python:{python_version}'
                )
                dockerfile.write_text(text)

            if (path / 'compose.yaml').exists():
                c.run('docker compose build')


@task
def test_sub(c):
    for path in iter_class_paths():
        print('test_sub:', path)
        with c.cd(str(path)):
            c.run('poetry install')
            c.run('poetry run task test')


@task
def win_test_last_class(c):
    code_path = Path('./codigo_das_aulas/13')
    with c.cd(str(code_path)):
        print('Current path: ', code_path)
        c.run('poetry install')
        c.run('poetry run task test')


@task
def win_test_migration(c):
    code_path = Path('./codigo_das_aulas/13')
    with c.cd(str(code_path)):
        print('Current path: ', code_path)
        c.run('poetry run alembic upgrade head')


@task
def command_sub(c, cmd):
    for path in iter_class_paths():
        print('command_sub:', path)
        with c.cd(str(path)):
            c.run(cmd)


@task
def update_sub(c):
    for path in iter_class_paths():
        toml = path / 'pyproject.toml'
        toml_tables = loads(toml.read_text())
        toml_project = toml_tables['project']
        dependencies = toml_project['dependencies']

        dev_dependencies = toml_tables['dependency-groups']['dev']

        print('update_sub:', path)
        with c.cd(str(path)):
            clean_venv_lock(c, path)

            for dep in sorted(dependencies):
                dep = dep.split()[0]
                print(dep, path)

                if dep in 'fastapi':
                    c.run('poetry add "fastapi[standard]@latest"')

                elif dep in 'pydantic':
                    c.run('poetry add "pydantic[email]@latest"')

                elif dep in 'pwdlib':
                    c.run('poetry add "pwdlib[argon2]@latest"')

                elif dep in 'psycopg':
                    c.run('poetry add "psycopg[binary]@latest"')

                else:
                    c.run(f'poetry add {dep}@latest')

            for dep in dev_dependencies:
                dep = dep.split()[0]
                c.run(f'poetry add --group dev {dep}@latest')

            c.run('poetry install')
