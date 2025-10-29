    ```yaml title=".github/workflows/pipeline.yaml" linenums="4" hl_lines="6-7"
    jobs:
      test:
        runs-on: ubuntu-latest
     
        steps:
          - name: Copia os arquivos do repositório
            uses: actions/checkout@v5
     
          - name: Instalar o python
            uses: actions/setup-python@v6
            with:
              python-version: '{{short_version}}'
     
          # continua com os passos anteriormente definidos
    ```
