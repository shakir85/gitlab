import gitlab
from config import Helper


def list_global_runners(*args, gl: gitlab.Gitlab) -> dict:
    """
    Get a list of specific config runners (admin) runners available to the user.
    :param gl: Gitlab object
    :return: A generator of dicts of runners data
    """
    ignored_items = ('description', 'ip_address', 'is_shared', 'name', 'is_shared', 'status', 'paused')

    scope = args[0]
    full = args[1]
    all = args[2]

    try:
        if not scope:
            for i in gl.runners_all.list() if all else gl.runners.list():
                if full:
                    yield i.attributes
                else:
                    shortened = {k: v for k, v in i.attributes.items() if k not in ignored_items}
                    yield shortened
        else:
            for i in gl.runners_all.list() if all else gl.runners.list(scope=scope):
                if full:
                    yield i.attributes
                else:
                    shortened = {k: v for k, v in i.attributes.items() if k not in ignored_items}
                    yield shortened

    except gitlab.exceptions.GitlabError as e:
        Helper.echo_error(msg=f"Gitlab API: {e}")


def describe_runner(runner_id: str, gl: gitlab.Gitlab) -> dict:
    """
    Get a runner’s detail:
    :param runner_id: Runner ID
    :param gl: Gitlab object
    :return: a dict of runner's full details
    """
    try:
        return gl.runners.get(runner_id).attributes

    except gitlab.exceptions.GitlabError as e:
        Helper.echo_error(msg=f"Gitlab API: {e}")
