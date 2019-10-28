from .request import Request


class GetContestData(Request):
    def __init__(self, contest_id: int):
        super().__init__()

        self.contest_id = contest_id

        self.path = "contest/{}".format(contest_id)
        self.method = "get"


class GetContestRank(Request):
    def __init__(self, contest_id: int):
        super().__init__()

        self.contest_id = contest_id

        self.path = "contest/rank/single/{}".format(contest_id)
        self.method = "get"
