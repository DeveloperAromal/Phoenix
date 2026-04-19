import json
import requests
from pathlib import Path
from config.settings import SCRAPER_API_KEY

class SocialOsint:
    
    def __init__(self, username: str, target_site: str):
        self.username = username
        self.target_site = target_site
    
    
    def _load_scraper_id_dataset(self) -> dict:
        base = Path.cwd()
        path = base / "phoenix" / "data" / "scraper_dataset.json"
        
        with open(path, "r") as f:
            data = json.load(f)
        
        return data
    
    
    def _load_url_dataset(self) -> dict:
        base = Path.cwd()
        path = base / "phoenix" / "data" / "site_url_dataset.json"
        
        with open(path, "r") as f:
            data = json.load(f)
        
        return data
    
    
    def _find_dataset_id(self) -> str:
        target = self.target_site 
        return self._load_scraper_id_dataset()[target]
    
    
    def _find_url(self) -> str:
        target = self.target_site  
        return self._load_url_dataset()[target]


    def _generate_paylod_url(self) -> dict:
        return {
            "input": [
                {"url": self._find_url().replace("{}", self.username)}
            ]
        }
        
    

    def osint(self):
        
        try:
            
            headers = {
                "Authorization": f"Bearer {SCRAPER_API_KEY}",
                "Content-Type": "application/json",
            }
                        

            res = requests.post(
                url="https://api.brightdata.com/datasets/v3/scrape", 
                headers=headers,
                params= {
                    "dataset_id": self._find_dataset_id(),
                    "notify": "false",
                    "include_errors": "true"
                }, 
                json = self._generate_paylod_url()
            )
            
            print(res.text)
        except requests.RequestException: 
            pass
        
        
        