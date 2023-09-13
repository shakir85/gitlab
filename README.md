# gl
This is a crappy CLI tool for getting things done with Gitlab runners. It's got the basics covered: listing, creating, and deleting ops, that's about it. I started this project mostly to teach myself the [Python Click library](https://click.palletsprojects.com/en/8.1.x/). Just so you know, it's not exactly a pet project I'm babysitting 24/7. I might toss in some more features down the road, but it's mostly just for kicks and giggles. If you're itching to explore how this tool works, well, here's how:

Clone the repo, then run
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
