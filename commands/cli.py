import click


@click.group("gl")
def cli():
    """
    This is the primary 'parent' CLI command. Resources like `runner`, `project` ...etc, are subgroups of this group.

    In the click lib, we can nest multiple groups together to create a command interface like this:
    $ gl [RESOURCE] [OPTIONS] COMMAND [ARGS]

    For example, to create a CLI tool to control various resources (e.g., Gitlab runners, projects,
    issues ... etc.), we need to nest click groups as the following:

        gl
        |-- runner
        |   |-- list
        |   |   `-- <ARGS>
        |   |-- update
        |   |   `-- <ARGS>
        |   `-- delete
        |       `-- <ARGS>
        `-- project
            |-- list
            |   `-- <ARGS>
            |-- update
            |   `-- <ARGS>
            `-- delete
                `-- <ARGS>

    Each subgroup in this package resides in its own *.py module. At the very top of each module,
    there is an import statement and a method call like this:
    ```
        from .cli import cli

        @cli.group("runner", cls=ClickAliasedGroup)
        def runner():
            pass
    ```
    This statement will call the cli() method (`gl` group) of this module and effectively nest
    the `runner` subgroup into the `gl` main group.

    Finally, the goal of this implementation is to keep the main command interface `$ gl ...`
    consistent across all the resources command-options. It's possible to let each resource implement
    its own main `gl` group but that's just plain stupid.

    I intentionally avoided creating a main class for the `gl` group and inherit from it
    just to keep things simple as much as possible.
    """
    pass
