from .request import Request


class LoginContest(Request):
    def __init__(self, contest_id: int, password: str):
        super().__init__()

        self.contest_id = contest_id
        self.password = password

        self.path = "contest/login/{}".format(contest_id)
        self.method = "post"

    def get_params(self):
        return {"password": self.password}
