    ```yaml title=".github/workflows/pipeline.yaml" linenums="1"
    name: Pipeline
    on: [push, pull_request]
     
    jobs:
      test:
        runs-on: ubuntu-latest
     
        steps:
          - name: Instalar o python
            uses: actions/setup-python@v6
            with:
              python-version: '{{short_version}}'
	```
