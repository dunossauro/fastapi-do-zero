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

## Ferramentas de gerenciamento do ambiente

```bash exec="1"
echo "- **Poetry**: $(poetry --version)"
echo "- **Pipx**: $(pipx --version)"
echo "- **Docker**: $(docker --version)"
echo "- **Docker-compose**: $(docker-compose --version)"
```
