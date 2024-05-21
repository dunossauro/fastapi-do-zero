from invoke import task
from rich import print
from pathlib import Path
from tomllib import loads


@task
def update_project(c):
    c.run('poetry update')


@task
def lint_sub(c):
    code_path = Path('./codigo_das_aulas/').resolve().glob('*')
    for path in sorted(code_path):
        print(path)
        with c.cd(str(path)):
            c.run(f'poetry run task lint')


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
            c.run(f'poetry install')
            c.run(f'poetry run task test')


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
            c.run(f'poetry update')
            c.run('rm -rf .venv')
            if (path / 'poetry.lock').exists():
                c.run('rm poetry.lock')

            for dep in sorted(dependencies):
                print(dep, path)
                if dep == 'pydantic':
                    c.run(f'poetry add "pydantic[email]@latest"')

                elif dep == 'passlib':
                    c.run(f'poetry add "passlib[bcrypt]@latest"')

                elif dep == 'psycopg':
                    c.run(f'poetry add "psycopg[binary]@latest"')

                elif dep == 'python':
                    ...

                else:
                    c.run(f'poetry add {dep}@latest')

            for dep in dev_dependencies:
                c.run(f'poetry add --group dev {dep}@latest')
