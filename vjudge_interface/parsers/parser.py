import json


class Parser:
    def parse_error(self, response):
        try:
            json_data = json.loads(response.text)
            if "error" in json_data:
                raise RuntimeError(json_data["error"])
        except:
            pass
