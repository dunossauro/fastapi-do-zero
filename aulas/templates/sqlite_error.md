??? warning "sqlalchemy.exc.OperationalError: (sqlite3.OperationalError)"
	Caso você receba esse erro ao aplicar a migração, recomendo que veja a [Live de Python #211](https://youtu.be/yQtqkq9UkDA) sobre `migrações e bancos de dados evolutivos` (recomendada no texto [da aula 04 - "Caso nunca tenha trabalhado com Migrações"](../04.md#instalando-o-alembic-e-criando-a-primeira-migracao){:target="_blank"}).

	No minuto [1:28:33](https://youtu.be/yQtqkq9UkDA?t=5313){:target="_blank"} o motivo e a solução desse erro são abordados em mais detalhes.

	Mas, em resumo, isso é um problema causado pelo modo como o python se comunica com o sqlite, fazendo com que cada alteração no banco seja aplicado linha, a linha.
	Para fazer todas as modificações de uma vez, usamos as `operações em batch`.
	A ideia é abrir uma única conexão com o banco de dados e executar determinadas operações para todas as linhas antes da conexão ser fechada.

	Para isso será preciso alterar o arquivo de migrações manualmente.
	O arquivo deve se parecer com esse:
	
    ```python title="/migrations/versions/bb77f9679811_exercicio_02_aula_04.py" linenums="20" hl_lines="3-4 15-16"
    # ...
    def upgrade():
        with op.batch_alter_table('users', schema=None) as batch_op:  #(1)!
            batch_op.add_column(   #(2)!
                sa.Column(
                    'updated_at',
                    sa.DateTime(),
                    server_default=sa.text('(CURRENT_TIMESTAMP)'),
                    nullable=False,
                )
            )
    
    
    def downgrade():
        with op.batch_alter_table('users', schema=None) as batch_op:  #(1)!
            batch_op.drop_column('updated_at')  #(3)!
    ```

    1. Entrando no contexto das operações em lote
    2. Adiciona a coluna `updated_at` na tabela `users` com o `batch_op`
    3. Remove a coluna `updated_at` da tabela `users` com o `batch_op`
