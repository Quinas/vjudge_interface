from .request import Request


class Login(Request):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.path = "user/login"
        self.method = "post"
        self.timeout = 5000

    def get_params(self):
        return {"username": self.username, "password": self.password}
