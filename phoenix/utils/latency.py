from datetime import datetime
from functools import wraps


def latency(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)   
        end = datetime.now()
        
        latency_time = end - start
        print(f"Latency: {latency_time}")
        
        return result                  
    
    return wrapper