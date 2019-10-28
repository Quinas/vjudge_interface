from .constants import ContestListCategory, Running, OrderDirection, ContestListOrderBy
from .request import Request


class GetContestList(Request):
    def __init__(
        self,
        start: int = 0,
        length: int = 20,
        title: str = "",
        owner: str = "",
        category: ContestListCategory = ContestListCategory.ALL,
        running: Running = Running.ALL,
        order_direction: OrderDirection = OrderDirection.DESCENDING,
        order_by: ContestListOrderBy = ContestListOrderBy.ID,
    ):
        super().__init__()

        self.start = start
        self.length = length
        self.title = title
        self.owner = owner
        self.category = category.value
        self.running = running.value
        self.order_direction = order_direction.value
        self.order_by = order_by.value

        self.path = "contest/data"
        self.method = "post"

    def get_params(self):
        return {
            "start": self.start,
            "length": self.length,
            "title": self.title,
            "owner": self.owner,
            "category": self.category,
            "running": self.running,
            "order[0][dir]": self.order_direction,
            "order[0][column]": self.order_by,
        }
