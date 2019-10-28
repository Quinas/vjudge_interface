from .request import Request


class GetUserProfile(Request):
    def __init__(self, username: str):
        super().__init__()

        self.username = username

        self.path = "user/{}".format(self.username)
        self.method = "get"
