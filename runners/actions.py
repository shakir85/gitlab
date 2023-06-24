import sys

import click
import gitlab
import os

try:
    gl = gitlab.Gitlab(private_token=os.environ['GITLAB_API_TOKEN'])
except Exception:
    print("Please export environment variable GITLAB_API_TOKEN=<TokenValue>")
    sys.exit(1)


def create_runner(registration_token: str):
    try:
        runner = gl.runners.create({'token': registration_token},
                                   run_untagged=False,
                                   tag_list=['tag1', 'tag2', 'tag3'],
                                   description='Provisioned via CLI tool - testing')
        print(runner)

    except gitlab.exceptions.GitlabError as e:
        click.echo(message="Error in Gitlab API:"
                           f"\n{e}", err=True)
