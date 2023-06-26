import click
from runners import data
from runners import action
from click_aliases import ClickAliasedGroup
from .cli import cli
from config import Helper

gitlab_obj = Helper.Config.gl


@cli.group("runner", cls=ClickAliasedGroup)
def runner():
    pass


@runner.command(aliases=["list", "ls"], help='List all runners.')
@click.option('--full', default=False, is_flag=True, help='Show more information about each runner.')
@click.option('--scope', default='', type=str, required=False, help='Runner scope. Accepted values are: active, paused, online')
@click.option('--all', '-a', default=False, is_flag=True, help='Get all runners in the Gitlab instance (specific and shared).')
def list_runner(scope, full, all) -> None:
    # Global runners only
    if full:
        r = data.list_global_runners(scope, True, all, gl=gitlab_obj)
    else:
        r = data.list_global_runners(scope, False, all, gl=gitlab_obj)
    for i in r:
        click.echo(i)


@runner.command(aliases=["describe", "desc"], help='Describe one or multiple runners.')
@click.option('--id', '-i', multiple=True, default=list, required=True, help="One or more runners ID")
def describe_runner(id) -> None:
    for i in id:
        r = data.describe_runner(runner_id=i, gl=gitlab_obj)
        click.echo(r)


@runner.command(aliases=["create"], help='Create a runner')
@click.option('--runner-token', '-t', default=str, required=True, help='Gitlab runner registration token.')
@click.option('--tag', multiple=True, default=list, required=False, help='Runner tag. Can pass multiple tags.')
@click.option('--description', '--desc', default=list, required=False, help='Runner description. Text must be quoted.')
def create_runner(description, runner_token, tag) -> None:
    action.create_runner(description, runner_token, gitlab_obj, tag)


@runner.command(aliases=["delete", "del"], help='Delete one or more runners.')
@click.option('--id', '-i', multiple=True, default=list, required=True, help='Delete one or more Gitlab runner ID.')
def delete_runner(id) -> None:
    for i in id:
        action.delete_runner(i, gitlab_obj)
