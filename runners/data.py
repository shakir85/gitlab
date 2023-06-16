"""
Wrappers for Gitlab API requests - Retrieve CI Runners data
"""
import requests


class RunnerDataException(Exception):
    pass


class RunnerData:
    def __init__(self, token):
        self.token: str = token
        self.headers: dict = {"PRIVATE-TOKEN": self.token}
        self.__base_url = "https://gitlab.com/api/v4/runners"

    def get_runners_data(self, all: bool = False, paused: bool = False, online_only: bool = False) -> list:
        try:
            url = self.__base_url

            if all:
                url = f"{self.__base_url}/all"
            if paused:
                url = f"{self.__base_url}?paused=true"
            if online_only:
                url = f"{self.__base_url}?status=online"

            r = requests.get(url, headers=self.headers)
            runners_metadata = r.json()
            return runners_metadata

        except Exception as e:
            response = requests.Response()
            response._content = b"Bad Request"
            response.reason = f"{e}"

    def get_runner_by_id(self, runner_id: str) -> dict:
        try:
            url = f"{self.__base_url}/{runner_id}"
            r = requests.get(url, headers=self.headers)
            runners_metadata = r.json()
            return runners_metadata

        except Exception as e:
            response = requests.Response()
            response._content = b"Bad Request"
            response.reason = f"{e}"
