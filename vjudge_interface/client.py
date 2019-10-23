import requests
import json
import urllib.parse
import vjudge_interface.requests as vrequests


class ApiClient:
    method_dict = {
        "get": requests.get,
        "post": requests.post,
        "put": requests.put,
        "delete": requests.delete,
    }

    def __init__(self, url_base, username=None, password=None):
        self.url_base = url_base
        self.username = username
        self.password = password
        self.cookies = {}

        if self.username is not None and self.password is not None:
            self.login(self.username, self.password)

    def send_request(self, request):
        args = {
            "url": self.__get_url(request),
            "params": request.get_params(),
            "data": json.dumps(request.get_body()),
            "timeout": request.timeout,
            "cookies": self.cookies,
        }

        return ApiClient.method_dict[request.method](**args)

    def login(self, username, password):
        self.username = username
        self.password = password
        self.cookies = self.send_request(
            vrequests.Login(self.username, self.password)
        ).cookies

    def __get_url(self, request):
        return urllib.parse.urljoin(self.url_base, request.path)
