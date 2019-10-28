from .request import Request


class GetGroupData(Request):
    def __init__(self, short_name: str):
        super().__init__()

        self.short_name = short_name

        self.path = "group/{}".format(short_name)
        self.method = "get"
