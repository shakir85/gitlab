# gl
This is my crappy CLI tool for working with Gitlab runners. It only provides a basic: list, create, and delete ops. I created this project mainly to teach myself the [Python Click library](https://click.palletsprojects.com/en/8.1.x/). This is not an actively maintained project. I may add more stuff to it but this project is really just for fun. You should always use the official Gitlab CLI. But if you're curious about how to use this tool, then this is how:

Clone the repo then run
```sh
python3 -m pip install --editable .
```

```sh
$ gl --help
Usage: gl [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  runner
```
See available options
```sh
$ gl runner --help
Usage: gl runner [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create-runner (create)          Create a global runner.
  delete-runner (del,delete)      Delete one or more runners.
  describe-runner (desc,describe)
                                  Describe one or multiple runners.
  list-runner (list,ls)           List all runners.
```
```
$ gl runner ls --help
Usage: gl runner ls [OPTIONS]

  List all runners.

Options:
  --full        Show more information about each runner.
  --scope TEXT  Runner scope. Accepted values are: active, paused, online
  -a, --all     Get all runners in the Gitlab instance (specific and shared).
  --help        Show this message and exit.
```
