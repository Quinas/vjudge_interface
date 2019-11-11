from requests_html import HTMLSession
import json
import urllib.parse
import vjudge_interface.requests as vrequests


class ApiClient:
    def __init__(self, url_base, username=None, password=None):
        self.url_base = url_base
        self.username = username
        self.password = password
        self.session = HTMLSession()
        self.method_dict = {
            "get": self.session.get,
            "post": self.session.post,
            "put": self.session.put,
            "delete": self.session.delete,
        }

        if self.username is not None and self.password is not None:
            self.login(self.username, self.password)

    def send_request(self, request):
        args = {
            "url": self.__get_url(request),
            "params": request.get_params(),
            "data": json.dumps(request.get_body()),
            "timeout": request.timeout,
        }

        response = self.method_dict[request.method](**args)
        return response

    def login(self, username, password):
        self.username = username
        self.password = password
        self.session.cookies.clear()
        self.send_request(vrequests.Login(self.username, self.password))

    def __get_url(self, request):
        return urllib.parse.urljoin(self.url_base, request.path)
