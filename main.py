from phoenix.utils.banner import Banner
from phoenix.utils.prompt_fn import PromptUser
from phoenix.modules.search.websearch import WebSearch
from phoenix.utils.logger import Logger
from phoenix.utils.config_helpers import ConfigHelper


def run_phoenix():
    
    Banner().phoenix_banner()
    config = ConfigHelper()

    while True:
        config.check()
        p = PromptUser("[#PHOENIX#] > ").collect()
        
        if p.lower() in ("quit", "exit", "q"):
            break
        
        queries = [
            "\"DeveloperAromal\" (site:linkedin.com OR site:twitter.com OR site:facebook.com OR site:instagram.com OR site:reddit.com)",
            "\"DeveloperAromal\" (site:github.com OR site:gitlab.com OR site:bitbucket.org OR site:stackoverflow.com)",
            "\"DeveloperAromal\" (cybersecurity OR \"software development\") (blog OR forum OR news)",
            "\"DeveloperAromal\" (breach OR leak OR pastebin OR \"exposed data\")",
            "\"DeveloperAromal\" (resume OR CV OR \"public record\" OR \"conference speaker\") filetype:pdf"
        ]
        
        for q in queries:
            Logger.info(f"\n[QUERY] {q}")
            
            res = WebSearch([q]).search()
            
            if not res.get("success"):
                Logger.error("No results or fetch failed")
                continue
            
            results = res.get("results", [])
            
            for r in results[:5]:   # safely limit to 5 results
                print(f"\n[+] {r.get('title', 'No Title')}")
                print(f"    {r.get('link', 'No Link')}")
                print(f"    {r.get('snippet', 'No Snippet')}")
            
            if not results:
                print("    No results found.")
                
run_phoenix()