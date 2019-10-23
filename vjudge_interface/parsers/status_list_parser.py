import json

STATUS_ITEM_PARAMS = {
    "memory": "memory",
    "access": "access",
    "execution_time": "runtime",
    "language": "language",
    "username": "userName",
    "user_id": "userId",
    "contest_id": "contestId",
    "contest_num": "contestNum",
    "processing": "processing",
    "run_id": "runId",
    "submission_time": "time",
    "OJ": "oj",
    "problem_id": "problemId",
    "source_length": "sourceLength",
    "problem_number": "probNum",
    "status": "status",
}


class StatusListParser:
    def parse(self, response):
        json_data = json.loads(response.text)
        data = []
        for status in json_data["data"]:
            status_dict = {}
            for key, idx in STATUS_ITEM_PARAMS.items():
                status_dict[key] = status[idx] if idx in status else None
            data.append(status_dict)
        return data
