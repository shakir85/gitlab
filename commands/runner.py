import click
from runners import data
from click_aliases import ClickAliasedGroup
from .cli import cli
from config import Helper

gitlab_obj = Helper.Config.gl


@cli.group("runner", cls=ClickAliasedGroup)
def runner():
    pass


@runner.command(aliases=["ls", "list"], help='List all runners.')
@click.option('--full', default=False, is_flag=True, help='Show more information about each runner.')
@click.option('--scope', default='', type=str, required=False, help='Runner scope. Accepted values are: active, paused, online')
@click.option('--all', '-a', default=False, is_flag=True, help='Get all runners in the Gitlab instance (specific and shared).')
def runner_ls(scope, full, all) -> None:
    # Global runners only
    if full:
        r = data.list_global_runners(scope, True, all, gl=gitlab_obj)
    else:
        r = data.list_global_runners(scope, False, all, gl=gitlab_obj)
    for i in r:
        click.echo(i)


@runner.command(aliases=["desc", "description"], help='Describe one or multiple runners.')
@click.option('--id', '-i', multiple=True, default=list, required=True)
def runner_desc(id: list) -> None:
    for i in id:
        r = data.describe_runner(runner_id=i, gl=gitlab_obj)
        click.echo(r)


""".option()
https://click.palletsprojects.com/en/8.1.x/options/
show_default=True
nargs=2
"""