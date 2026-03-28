from config.settings import PROXIES_PATH

import os
import random
import requests



class ProxyRotator:
    
    def __init__(self):
        pass
    
    
    def _load_proxy(self):
        path = os.path.abspath(PROXIES_PATH)
        
        with open(path, "r") as fs:
            proxy = fs.readlines()
            return proxy
    
    def _detect_proto(self, ip_proxy):
        
        for proto in ["http", "socks5", "socks4"]:
            proxy = f"{proto}://{ip_proxy}"
            try:
                res = requests.get(
                    "https://httpbin.org/ip",
                    proxies={"http": proxy, "https": proxy},
                    timeout=5
                )
                if res.status_code == 200:
                    return proto
            except:
                continue
        return None 
        
    def rotate(self):
        rand_proxy = random.choice(self._load_proxy()).strip()
        
        proto = self._detect_proto(rand_proxy)
        
        if not proto:
            return None
        
        proxy = f"{proto}://{rand_proxy}"
        return {
            "http": proxy,
            "https": proxy
        }
        
