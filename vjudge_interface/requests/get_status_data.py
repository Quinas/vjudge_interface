from .request import Request


class GetStatusData(Request):
    def __init__(self, status_id: int):
        super().__init__()

        self.status_id = status_id

        self.path = "solution/data/{}".format(status_id)
        self.method = "post"
