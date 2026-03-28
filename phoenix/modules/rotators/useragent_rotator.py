from config.settings import USER_AGENTS_PATH

import os
import random

class UARotator:
    
    def __init__(self):
        pass
    
    
    def _load_user_agent(self):
        path = os.path.abspath(USER_AGENTS_PATH)
        
        with open(path, "r") as fs:
            agents = fs.readlines()
            return agents
    
        
    def rotate(self):
        return random.choice(self._load_user_agent()).replace("\n", "").strip()