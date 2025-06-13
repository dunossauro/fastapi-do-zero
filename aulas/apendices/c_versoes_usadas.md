# C - Versões das bibliotecas

{% include "templates/versoes.md" %}

## Bibliotecas do projeto

```toml
--8<-- "codigo_das_aulas/13/pyproject.toml:10:21"
```

## Bibliotecas de desenvolvimento

```toml
--8<-- "codigo_das_aulas/13/pyproject.toml:23:32"
```

### Lock de todo o ambiente

O lock do projeto final pode ser encontrado [aqui!](https://github.com/dunossauro/fastapi-do-zero/blob/{{current_tag}}/codigo_das_aulas/13/poetry.lock){:target="_blank"}

## Ferramentas de gerenciamento do ambiente

```bash exec="1"
echo "- **Poetry**: $(poetry --version)"
echo "- **Pipx**: $(pipx --version)"
echo "- **Docker**: $(docker --version)"
echo "- **Docker-compose**: $(docker-compose --version)"
echo "- **Flyctl**: $(flyctl version)"
```
