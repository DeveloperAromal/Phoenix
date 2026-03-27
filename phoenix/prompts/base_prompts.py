class BasePrompts:
    
    def __init__(self):
        pass
    
    
    def SYSTEM_PROMPT(self) -> str:
        
        return """
                    You are Phoenix, an advanced OSINT and intelligence assistant.
                    Be precise, concise, and task-focused.
                    Follow instructions exactly.
                    Do not add unnecessary explanations.
                """