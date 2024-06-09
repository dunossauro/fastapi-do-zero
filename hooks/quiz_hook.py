import markdown
import ast


def format_quiz(source, *args, **kwargs):
    block = ast.literal_eval(source)

    code = markdown.markdown(
        block['code'],
        extensions=['pymdownx.superfences'],
    )

    ops = []
    for chave, valor in block['opcoes'].items():
        if chave == block['correta']:
            ops.append(
                f"""
            <div>
            <input type="radio" name="answer" value="{valor}" id="{chave}" correct="">
            <label for="{chave}">{valor}</label>
            </div>
            """
            )
        else:
            ops.append(
                f"""
            <div>
            <input type="radio" name="answer" value="{valor}" id="{chave}">
            <label for="{chave}">{valor}</label>
            </div>
            """
            )

    return f"""
    <div class="quiz"><h3>{block["questao"]}</h3>
    {code}
    <form>
    <fieldset>
    {'\n'.join(ops)}
    </fieldset>
    <button type="submit" class="quiz-button">Enviar</button>
    </form>
    <section class="content hidden"></section>
    </div>
    """


def on_page_markdown(markdown_text, *args, **kwargs):
    if '```quiz' in markdown_text:
        md = markdown.markdown(
            markdown_text,
            extensions=['pymdownx.superfences'],
            extension_configs={
                'pymdownx.superfences': {
                    'custom_fences': [
                        {'name': 'quiz', 'class': 'quiz', 'format': format_quiz}
                    ]
                }
            },
        )
        return md


def on_page_content(html, *args, **kwargs):
    return html.replace('Submit', 'Enviar')
