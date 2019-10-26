import json


class Parser:
    def parse_error(self, response):
        try:
            json_data = json.loads(response.text)
            if "error" in json_data:
                return {"_error": json_data["error"]}
            return None
        except:
            return None
