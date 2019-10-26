from .request import Request


class GetContestData(Request):
    def __init__(self, contest_id: int, password: str = None):
        self.contest_id = contest_id
        self.password = password

        if password is None:
            self.path = "contest/rank/single/{}".format(contest_id)
            self.method = "get"

        else:
            self.path = "contest/login/{}".format(contest_id)
            self.method = "post"

        self.timeout = 5000

    def get_params(self):
        if self.password is not None:
            return {"password": self.password}

        return {}
