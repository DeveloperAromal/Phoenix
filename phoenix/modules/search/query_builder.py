from phoenix.prompts.tools_prompt import QUERY_BUIlDER_PROMPT
from phoenix.prompts.base_prompts import BasePrompts
from phoenix.utils.llm import ChatLLM

class QueryBuilder:
    
    def __init__(self, ch_sketch: str):
        self.ch_sketch = ch_sketch
    
    
    
    def _load_prompt(self):
        return QUERY_BUIlDER_PROMPT().query_builder_prompt(self.ch_sketch)
    
    def _load_system_prompt(self):
        return BasePrompts().SYSTEM_PROMPT()
    
    
    def query(self):
        
        llm = ChatLLM(
            model="",
            api_base_url="",
            api_key=""
        )
        
        query = llm.invoke(
            prompt=self._load_prompt(),
            system_prompt=self._load_system_prompt(),
            max_tokens=500,
            temperature=0.7
        )
        
        return query