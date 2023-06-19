# pipenv run python runners.py [OPTIONS] COMMAND [ARGS]
"""
CLI commands for managing runners
"""
import click
from runners import data


@click.group("gl")
def cli():
    pass


@cli.group("runner")
def runner():
    pass


@runner.command(name="ls")
def runner_ls():
    r = data.get_runners_data()
    for i in r:
        print(i)
