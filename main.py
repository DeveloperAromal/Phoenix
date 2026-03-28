from phoenix.utils.banner import Banner
from phoenix.utils.prompt_fn import PromptUser
from phoenix.modules.search.query_builder import QueryBuilder
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
        
        query = QueryBuilder(p).query()
        
        Logger().success(query)

run_phoenix()