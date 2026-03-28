from phoenix.memory.cache_storage import URL_CRAWL_CACHE
from .url_crafter import CraftURL
from bs4 import BeautifulSoup
import requests


class CrawlURL:
    
    def __init__(self):
        self.crafter = CraftURL()
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def crawl(self, username: str):
        urls = self.crafter.urls(username)
        results = {}

        for name, url in urls.items():
            try:
                res = requests.get(url, headers=self.headers, timeout=10)

                data = {
                    "url": url,
                    "status_code": res.status_code,
                    "final_url": res.url
                }

                if res.status_code == 200:
                    soup = BeautifulSoup(res.text, "html.parser")

                    title = soup.title.string.strip() if soup.title and soup.title.string else ""
                    description = ""

                    desc_tag = soup.find("meta", attrs={"name": "description"})
                    if desc_tag and desc_tag.get("content"):
                        description = desc_tag["content"].strip()

                    data.update({
                        "status": "success",
                        "title": title,
                        "description": description
                    })
                else:
                    data["status"] = "failed"

                results[name] = data

            except Exception as e:
                results[name] = {
                    "url": url,
                    "status": "error",
                    "error": str(e)
                }

        URL_CRAWL_CACHE[username] = results

        return results