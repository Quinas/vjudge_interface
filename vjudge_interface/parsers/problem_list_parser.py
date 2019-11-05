import json
import bs4

from .parser import Parser


class ProblemListParser(Parser):
    """
    [
        {'username': 'user1', 'nickname': 'nick', 'school': 'myschool', 'solved': 0},
        {'username': 'user2', 'nickname': 'nick2', 'school': None, 'solved': 2},
        ...
    ]
    """

    def parse(self, response):
        self.parse_error(response)

        json_data = json.loads(response.text)
        data = []

        for problem in json_data["data"]:
            source = ""
            source_href = ""
            if "source" in problem:
                soup = bs4.BeautifulSoup(problem["source"], "html.parser")
                a = soup.find("a")
                if a is not None:
                    source = a.text
                    source_href = a["href"]
                else:
                    source = soup.text

            data.append(
                {
                    "id": problem["id"],
                    "title": problem["title"],
                    "OJ": problem["originOJ"],
                    "origin_id": problem["originProb"],
                    "allow_submit": problem["allowSubmit"],
                    "update_time": problem["triggerTime"],
                    "source": source,
                    "source_href": source_href,
                    "status": problem["status"],
                }
            )

        return data
