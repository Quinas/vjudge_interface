from .constants import (
    OnlineJudge,
    OrderDirection,
    ProblemListCategory,
    ProblemListOrderBy,
)
from .request import Request


class GetProblemList(Request):
    def __init__(
        self,
        start: int = 0,
        length: int = 20,
        OJ: OnlineJudge = OnlineJudge.ALL,
        problem_number: str = "",
        title: str = "",
        origin: str = "",
        category: ProblemListCategory = ProblemListCategory.ALL,
        order_direction: OrderDirection = OrderDirection.DESCENDING,
        order_by: ProblemListOrderBy = ProblemListOrderBy.UPDATE_TIME,
    ):
        self.start = start
        self.length = length
        self.OJ = OJ.value
        self.problem_number = problem_number
        self.title = title
        self.origin = origin
        self.category = category
        self.order_direction = order_direction.value
        self.order_by = order_by.value

        self.path = "problem/data"
        self.method = "post"
        self.timeout = 5000

    def get_params(self):
        return {
            "start": self.start,
            "length": self.length,
            "OJId": self.OJ,
            "probNum": self.problem_number,
            "title": self.title,
            "source": self.origin,
            "category": self.category,
            "order[0][column]": self.order_by,
            "order[0][dir]": self.order_direction,
        }
