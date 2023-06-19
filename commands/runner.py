import click
from runners import data
from click_aliases import ClickAliasedGroup
from .cli import cli


@cli.group("runner", cls=ClickAliasedGroup)
def runner():
    pass


@runner.command(aliases=["ls", "list"], help='List all runners.')
@click.option('--full', is_flag=True, help='Show more information about each runner.')
def runner_ls(full) -> None:
    if full:
        r = data.get_runners_data(short=False)
    else:
        r = data.get_runners_data(short=True)
    for i in r:
        click.echo(i)


@runner.command(aliases=["desc", "description"], help='Describe one or multiple runners.')
@click.option('--id', '-i', multiple=True, default=list)
def runner_desc(id: list) -> None:
    for i in id:
        r = data.describe_runner(runner_id=i)
        click.echo(r)
