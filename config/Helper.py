import click
import gitlab
import sys
import os

""" Text Decoration """
# Formatting
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALICS = '\033[3m'

# Colors
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = u'\033[33m'


def echo_error(msg):
    click.echo(message=f"{RED}=> Error:{END} {msg}")


def echo_info(msg):
    click.echo(message=f"{GREEN}=> Info:{END} {msg}")


def echo_warning(msg):
    click.echo(message=f"{YELLOW}=> Warning:{END} {msg}")


def echo_note(msg):
    click.echo(message=f"{ITALICS}{BLUE}Note: {msg}")


class HelperException(Exception):
    pass


class Config:
    try:
        gl = gitlab.Gitlab(private_token=os.environ['GITLAB_API_TOKEN'])
    except KeyError:
        print("Please export environment variable GITLAB_API_TOKEN=<TokenValue>")
        sys.exit(1)


class Init:
    pass
