import os
import runners
from pprint import pprint


def main():
    gl_token = os.environ['GITLAB_API_TOKEN']
    a = runners.actions.RunnerActions(token=gl_token)
    d = runners.data.RunnerData(token=gl_token)

    pprint(
        d.get_runners_data()
    )


if __name__ == '__main__':
    main()
