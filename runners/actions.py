import click
import gitlab


def create_runner(registration_token: str, gl: gitlab.Gitlab):
    try:
        runner = gl.runners.create({'token': registration_token},
                                   run_untagged=False,
                                   tag_list=['tag1', 'tag2', 'tag3'],
                                   description='Provisioned via CLI tool - testing')
        print(runner)

    except gitlab.exceptions.GitlabError as e:
        click.echo(message="Error in Gitlab API:"
                           f"\n{e}", err=True)
