from .constants import OnlineJudge, Result, Language
from .request import Request


class GetStatusList(Request):
    def __init__(
        self,
        start: int = 0,
        length: int = 20,
        username: str = "",
        OJ: OnlineJudge = OnlineJudge.ALL,
        problem: str = "",
        result: Result = Result.ALL,
        language: Language = Language.ALL,
        only_followed: bool = False,
    ):
        self.start = start
        self.length = length
        self.username = username
        self.OJ = OJ.value
        self.problem = problem
        self.result = result.value
        self.language = language.value
        self.only_followed = only_followed

        self.path = "status/data"
        self.method = "post"
        self.timeout = 5000

    def get_params(self):
        return {
            "start": self.start,
            "length": self.length,
            "un": self.username,
            "OJId": self.OJ,
            "probNum": self.problem,
            "result": self.result,
            "language": self.language,
            "onlyFollowee": self.only_followed,
        }
