    ```yaml title=".github/workflows/pipeline.yaml" linenums="8"
        steps:
          - name: Instalar o python
            uses: actions/setup-python@v6
            with:
              python-version: '{{short_version}}'
     
          - name: Instalar o poetry
            run: pipx install poetry
     
          - name: Instalar dependências
            run: poetry install
     
          - name: Executar testes
            run: poetry run task test
    ```
