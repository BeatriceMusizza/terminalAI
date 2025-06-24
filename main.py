import click
from history import add_to_history, get_history

from modules.qa import run as qa_run
from modules.explain import run as explain_run
from modules.rephrase import run as rephrase_run
from modules.doc_gen import run as doc_run

@click.group()
def cli():
    pass

@cli.command()
@click.argument("question")
@click.option("--profession", default="general", help="Answer as if you are this professional")
def qa(question, profession):
    reply = qa_run(question, profession)
    add_to_history(question, reply)
    print(reply)

@cli.command()
@click.argument("command")
def explain(command):
    reply = explain_run(command)
    add_to_history(command, reply)
    print(reply)

@cli.command()
@click.argument("text")
@click.option("--style", default="formal", help="Writing style")
@click.option("--tone", default=None, help="Tone of voice (e.g., persuasive, friendly)")
@click.option("--audience", default=None, help="Target audience (e.g., kids, scientists)")
def rephrase(text, style, tone, audience):
    reply = rephrase_run(text, style, tone, audience)
    add_to_history(text, reply)
    print(reply)

@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--scope", type=click.Choice(["functions", "general", "both"]), default="both", help="Level of documentation detail")
def doc(file, scope):
    reply = doc_run(file, scope)
    add_to_history(f"Documentation request for {file} ({scope})", reply)
    print(reply)

@cli.command()
def history():
    for i, (q, r) in enumerate(get_history()):
        print(f"{i+1}. Q: {q}\n   A: {r}\n")

if __name__ == "__main__":
    cli()
