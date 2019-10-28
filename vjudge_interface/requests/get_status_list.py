from .constants import OnlineJudge, Result, Language
from .request import Request


class GetStatusList(Request):
    def __init__(
        self,
        start: int = 0,
        length: int = 20,
        username: str = "",
        contest_id: int = "",
        OJ: OnlineJudge = OnlineJudge.ALL,
        problem: str = "",
        result: Result = Result.ALL,
        language: Language = Language.ALL,
        only_followed: bool = False,
        in_contest: bool = False,
    ):
        super().__init__()

        self.start = start
        self.length = length
        self.username = username
        self.contest_id = contest_id
        self.OJ = OJ.value
        self.problem = problem
        self.result = result.value
        self.language = language.value
        self.only_followed = only_followed
        self.in_contest = in_contest

        self.path = "status/data"
        self.method = "post"

    def get_params(self):
        return {
            "start": self.start,
            "length": self.length,
            "un": self.username,
            "contestId": self.contest_id,
            "OJId": self.OJ,
            "probNum": self.problem,
            "res": self.result,
            "language": self.language,
            "onlyFollowee": self.only_followed,
            "inContest": self.in_contest,
        }
