import sys

import click
import gitlab
import os

try:
    gl = gitlab.Gitlab(private_token=os.environ['GITLAB_API_TOKEN'])
except Exception:
    print("Please export environment variable GITLAB_API_TOKEN=<TokenValue>")
    sys.exit(1)


def list_global_runners(scope: str = "", full: bool = False, all: bool = False) -> dict:
    """
    Get a list of specific global runners (admin) runners available to the user.
    :param all: Get a list of all runners in the GitLab instance (specific and shared). Access is restricted to users with administrator access.
    :param scope: Filter the list based on the runner status. Accepted values are: 'active', 'paused', 'online'
    :param full: Show complete runner's dict data
    :return: A generator for dicts of runners data
    """
    shortlist = ('description', 'ip_address', 'is_shared', 'name', 'is_shared', 'status', 'paused')
    try:
        if not scope:
            for i in gl.runners_all.list() if all else gl.runners.list():
                if full:
                    yield i.attributes
                else:
                    shortened = {k: v for k, v in i.attributes.items() if k not in shortlist}
                    yield shortened
        else:
            for i in gl.runners_all.list() if all else gl.runners.list(scope=scope):
                if full:
                    yield i.attributes
                else:
                    shortened = {k: v for k, v in i.attributes.items() if k not in shortlist}
                    yield shortened

    except gitlab.exceptions.GitlabError as e:
        click.echo(message="Error in Gitlab API:"
                           f"\n{e}", err=True)


def describe_runner(runner_id: str) -> dict:
    """
    Get a runner’s detail:
    :param runner_id: Runner ID
    :return: a dict of runner's full details
    """
    try:
        return gl.runners.get(runner_id).attributes

    except gitlab.exceptions.GitlabError as e:
        click.echo(message="Error in Gitlab API:"
                           f"\n{e}", err=True)
