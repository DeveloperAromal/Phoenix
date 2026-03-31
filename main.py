import json
import os
from datetime import datetime
from phoenix.utils.banner import Banner
from phoenix.utils.prompt_fn import PromptUser
from phoenix.modules.search.websearch import WebSearch
from phoenix.utils.logger import Logger
from phoenix.utils.config_helpers import ConfigHelper
from phoenix.modules.normalizer.normalize_websearch import Normalizer
from phoenix.modules.transformer.url_crawler import CrawlURL
from phoenix.memory.cache_storage import URL_CRAWL_CACHE
from phoenix.modules.rotators.proxy_rotator import ProxyRotator



def save_report(data):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/recon_{timestamp}.json"
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
           
            if isinstance(data, str):
                f.write(data)
            else:
                json.dump(data, f, indent=4)
        Logger.info(f"Intelligence report saved to: {filename}")
    except Exception as e:
        Logger.error(f"Failed to save file: {e}")

def run_phoenix():
    Banner().phoenix_banner()
    config = ConfigHelper()

    while True:
        config.check()
        p = PromptUser("[#PHOENIX#] > ").collect()
        
        if p.lower() in ("quit", "exit", "q"):
            break
        
        # queries = [
        #     "\"DeveloperAromal\" (site:linkedin.com OR site:twitter.com OR site:facebook.com OR site:instagram.com OR site:reddit.com)",
        #     "\"DeveloperAromal\" (site:github.com OR site:gitlab.com OR site:bitbucket.org OR site:stackoverflow.com)",
        #     "\"DeveloperAromal\" (cybersecurity OR \"software development\") (blog OR forum OR news)",
        #     "\"DeveloperAromal\" (breach OR leak OR pastebin OR \"exposed data\")",
        #     "\"DeveloperAromal\" (resume OR CV OR \"public record\" OR \"conference speaker\") filetype:pdf"
        # ]
        
        # session_intelligence = []
        
        # for q in queries:
        #     Logger.info(f"\n[*] Scanning: {q}")
        #     search_engine = WebSearch([q])
        #     res = search_engine.search()
            
        #     if res.get("success"):
        #         session_intelligence.append(res)
        #     else:
        #         Logger.error(f"No data for: {q}")

        # if session_intelligence:
        #     Logger.info("\n[*] Finalizing Reconnaissance...")
        #     full_context = json.dumps(session_intelligence)
            
        #     try:
        #         normalized_report = Normalizer(full_context).norm()
                
        #         print("\n[PHOENIX FINAL INTELLIGENCE REPORT]")
        #         print(normalized_report)
                
        #         save_report(normalized_report)
                
        #     except Exception as e:
        #         Logger.error(f"Normalization or Saving failed: {e}")
        # else:
        #     Logger.error("No intelligence gathered.")
            
        p = CrawlURL().crawl("")
        print(p)
        # ProxyRotator().rotate()
if __name__ == "__main__":
    run_phoenix()