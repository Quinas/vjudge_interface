from .request import Request


class Login(Request):
    def __init__(self, username: str, password: str):
        super().__init__()

        self.username = username
        self.password = password

        self.path = "user/login"
        self.method = "post"

    def get_params(self):
        return {"username": self.username, "password": self.password}
