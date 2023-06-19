import click
from runners import data
from click_aliases import ClickAliasedGroup


@click.group("gl")
def cli():
    pass


@cli.group("runner", cls=ClickAliasedGroup)
def runner():
    pass


@runner.command(aliases=["ls", "list"])
def runner_ls():
    r = data.get_runners_data()
    for i in r:
        click.echo(i)


@runner.command(aliases=["desc", "description"])
@click.option('--id', '-i', multiple=True, default=list, help='Describe one or multiple runners')
def runner_desc(id: list):
    for i in id:
        r = data.describe_runner(runner_id=i)
        click.echo(r)
