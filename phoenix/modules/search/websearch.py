from langchain_community.tools import DuckDuckGoSearchRun

class WebSearch:
    def __init__(self, query: str | list):
        if isinstance(query, list):
            self.query = query[0]
        else:
            self.query = query

    def search(self):
        tool = DuckDuckGoSearchRun()
        try:
            raw_data = tool.run(str(self.query))
            return {
                "success": True, 
                "results": [{"title": "Search Result", "link": "N/A", "snippet": raw_data}]
            }
        except Exception:
            return {"success": False, "results": []}