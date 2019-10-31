from .parser import Parser

import bs4
import json


class ProblemDataParser(Parser):
    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        self.data = {}
        self.soup = bs4.BeautifulSoup(response.text, "html.parser")
        self._json_data()
        self._properties()
        return self.data

    def _json_data(self):
        json_data = json.loads(self.soup.find("textarea", {"name": "dataJson"}).text)
        self.data["allow_submit"] = json_data["allowSubmit"]
        self.data["id"] = json_data["problemId"]
        self.data["is_favorite"] = json_data["isFav"]
        self.data["status"] = json_data["status"]

    def _properties(self):
        properties = self.soup.find("div", id="prob-properties").div.dl
        dt = properties.find_all("dt")
        dd = properties.find_all("dd")

        self.data["properties"] = {}
        for idx in range(len(dt)):
            self.data["properties"][dt[idx].text] = dd[idx].text
