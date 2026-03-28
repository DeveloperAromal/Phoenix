from phoenix.utils.banner import Banner
from phoenix.utils.prompt_fn import PromptUser



def run_phoenix():
    
    Banner().phoenix_banner()
    
    while True:
        p = PromptUser("[#PHOENIX#] > ").collect()
        
        if p.lower() in ("quit", "exit", "q"):
            break


run_phoenix()