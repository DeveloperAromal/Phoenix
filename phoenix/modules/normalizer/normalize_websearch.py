from phoenix.prompts.tools_prompt import ToolPrompts
from phoenix.prompts.base_prompts import BasePrompts

from phoenix.utils.llm import ChatLLM
from config.settings import (
    LLM_API_KEY,
    LLM_MODEL,
    LLM_BASE_URL
)
from phoenix.memory.cache_storage import API_KEY_CACHED


class Normalizer:
    
    def __init__(self, web_ser_res: dict):
        self.web_ser_res = web_ser_res
    
    def _load_prompt(self):
        return ToolPrompts().NORMALIZE_DATA_PROMPT(self.web_ser_res)
    
    
    def _system_prompt(self):
        return BasePrompts().SYSTEM_PROMPT()
    
    
    def norm(self):
        
        llm = ChatLLM(
            model=LLM_MODEL,
            api_base_url=LLM_BASE_URL,
            api_key=API_KEY_CACHED[0] if API_KEY_CACHED else LLM_API_KEY
        )
        

        norm_data = llm.invoke(
            prompt=self._load_prompt(),
            system_prompt=self._system_prompt(),
            max_tokens=8000,
            temperature=0.1
        )
        
        return norm_data