from .request import Request


class GetUserProfile(Request):
    def __init__(self, username: str):
        self.username = username

        self.path = "user/{}".format(self.username)
        self.method = "get"
        self.timeout = 5000
