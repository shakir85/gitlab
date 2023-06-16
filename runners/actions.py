"""
Wrappers for Gitlab API requests - Perform actions on CI Runners
"""


class RunnerActionsException(Exception):
    pass


class RunnerActions:
    def __init__(self, token):
        self.token: str = token
        self.headers: dict = {"PRIVATE-TOKEN": self.token}
        self.__base_url = "https://gitlab.com/api/v4/runners"

    def print_data(self):
        print(self.headers)

