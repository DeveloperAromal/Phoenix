from phoenix.prompts.tools_prompt import ToolPrompts
from phoenix.prompts.base_prompts import BasePrompts
from config.settings import (
    LLM_API_KEY,
    LLM_BASE_URL,
    LLM_MODEL,
)
from phoenix.memory.cache_storage import API_KEY_CACHED
from phoenix.utils.llm import ChatLLM

class QueryBuilder:
    
    def __init__(self, ch_sketch: str):
        self.ch_sketch = ch_sketch
    
    
    
    def _load_prompt(self):
        return ToolPrompts().QUERY_BUIlDER_PROMPT(self.ch_sketch)
    
    def _load_system_prompt(self):
        return BasePrompts().SYSTEM_PROMPT()
    
    
    def query(self):
        
        llm = ChatLLM(
            model=LLM_MODEL,
            api_base_url=LLM_BASE_URL,
            api_key = API_KEY_CACHED[0] if API_KEY_CACHED else LLM_API_KEY        
        )
        
        query = llm.invoke(
            prompt=self._load_prompt(),
            system_prompt=self._load_system_prompt(),
            max_tokens=500,
            temperature=0.7
        )
        
        return query