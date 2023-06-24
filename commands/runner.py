import click
from runners import data
from click_aliases import ClickAliasedGroup
from .cli import cli


@cli.group("runner", cls=ClickAliasedGroup)
def runner():
    pass


@runner.command(aliases=["ls", "list"], help='List all runners.')
@click.option('--full', default=False, is_flag=True, help='Show more information about each runner.')
@click.option('--scope', default='', type=str, required=False, help='Runner scope. Accepted values are: active, paused, online')
@click.option('--all', '-a', default=False, is_flag=True, help='Get all runners in the Gitlab instance (specific and shared).')
def runner_ls(full, scope, all) -> None:
    # Global runners only
    if full:
        r = data.list_global_runners(full=True, scope=scope, all=all)
    else:
        r = data.list_global_runners(full=False, scope=scope, all=all)
    for i in r:
        click.echo(i)


@runner.command(aliases=["desc", "description"], help='Describe one or multiple runners.')
@click.option('--id', '-i', multiple=True, default=list, required=True)
def runner_desc(id: list) -> None:
    for i in id:
        r = data.describe_runner(runner_id=i)
        click.echo(r)


""".option()
https://click.palletsprojects.com/en/8.1.x/options/
show_default=True
nargs=2
"""