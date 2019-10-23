from .constants import TimeRange
from .request import Request


class GetUserList(Request):
    def __init__(
        self,
        start: int = 0,
        length: int = 20,
        username: str = "",
        nickname: str = "",
        school: str = "",
        time_range: TimeRange = TimeRange.TIME_24HOURS,
    ):
        self.start = start
        self.length = length
        self.username = username
        self.nickname = nickname
        self.school = school
        self.time_range = time_range.value

        self.path = "user/data"
        self.method = "post"
        self.timeout = 5000

    def get_params(self):
        return {
            "start": self.start,
            "length": self.length,
            "username": self.username,
            "nickname": self.nickname,
            "school": self.school,
            "statRange": self.time_range,
        }
