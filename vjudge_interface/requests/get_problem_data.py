from .request import Request


class GetProblemData(Request):
    def __init__(self, problem_id: int):
        super().__init__()

        self.problem_id = problem_id

        self.path = "problem/{}".format(problem_id)
        self.method = "get"
