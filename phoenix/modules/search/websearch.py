from langchain_community.tools import DuckDuckGoSearchResults
import json

class WebSearch:
    def __init__(self, query: str | list):
        if isinstance(query, list):
            self.query = query[0]
        else:
            self.query = query
        self.last_results = None

    def search(self):
        tool = DuckDuckGoSearchResults()
        try:
            raw_data = tool.run(str(self.query))
            self.last_results = {
                "success": True,
                "query": self.query,
                "results": [
                    {
                        "title": "Search Result",
                        "link": "N/A",
                        "snippet": raw_data
                    }
                ]
            }
        except Exception:
            self.last_results = {
                "success": False,
                "query": self.query,
                "results": []
            }
        return self.last_results

    def to_json(self):
        data = self.last_results if self.last_results else self.search()
        return json.dumps(data, indent=4)