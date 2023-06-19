import sys

import gitlab
import os

try:
    gl = gitlab.Gitlab(private_token=os.environ['GITLAB_API_TOKEN'])
except Exception:
    print("Please export environment variable GITLAB_API_TOKEN=<TokenValue>")
    sys.exit(1)


def get_runners_data(short: bool = True) -> dict:
    shortlist = ('description', 'ip_address', 'is_shared', 'name', 'is_shared', 'status', 'paused')
    if short:
        for i in gl.runners.list():
            shortened = {k: v for k, v in i.attributes.items() if k not in shortlist}
            yield shortened
    else:
        for i in gl.runners.list():
            yield i.attributes


def describe_runner(runner_id: str) -> dict:
    return gl.runners.get(runner_id).attributes
