import gitlab
import sys
import os


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
