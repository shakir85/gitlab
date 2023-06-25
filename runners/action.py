import click
import gitlab
from config import Helper


def create_runner(desc: str = '', *args):
    """
    Creates a Gitlab Runner.
    :param desc: Runner description
    :param args:
        1. Gitlab Runner registration token,
        2. Gitlab API object.
        3. Runner tags list
    """
    registration_token: str = args[0]
    gl: Helper.Config.gl = args[1]
    tags: list = args[2]

    try:
        runner = gl.runners.create({'token': registration_token,
                                    'run_untagged': 'no',
                                    'tag_list': [i for i in tags],
                                    'description': desc})
        Helper.echo_info(msg=f"Runner created - id: {runner.attributes['id']}")
        Helper.echo_note(msg="\nRunner will be inactive on Gitlab UI if not runner installed on this host.")
        return runner.attributes

    except gitlab.exceptions.GitlabCreateError as e:
        Helper.echo_error(msg=f"Gitlab API: {e}")


def delete_runner(*args):
    """
    Deletes a Gitlab Runner.
    :param args:
        1. Gitlab Runner ID
        2. Gitlab API object.
    """
    runner_id: int = args[0]
    gl: Helper.Config.gl = args[1]

    try:
        gl.runners.delete(runner_id)
        Helper.echo_info(msg=f"Runner deleted - id: {runner_id}")

    except gitlab.exceptions.GitlabDeleteError as e:
        Helper.echo_error(msg=f"Gitlab API: runner ID {runner_id} - {e} ")
