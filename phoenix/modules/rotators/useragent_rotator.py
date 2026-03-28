from config.settings import USER_AGENTS_PATH

import os
import random
import requests



class ProxyRotator:
    
    def __init__(self):
        pass
    
    
    def _load_user_agent(self):
        path = os.path.abspath(USER_AGENTS_PATH)
        
        with open(path, "r") as fs:
            agents = fs.readlines()
            return agents
    
        
    def rotate(self):
        rand_agent = random.choice(self._load_agent())
        rand_agent.strip()

        return rand_agent