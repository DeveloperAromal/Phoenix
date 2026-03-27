

class ToolPrompts:
    
    def __init__(self):
        pass
    
    
    def QUERY_BUIlDER_PROMPT(self, ch_sketch: str) -> str:
        
        return f"""
                    You are an OSINT query builder inside Phoenix, an advanced reconnaissance and intelligence framework.
                    Your task is to generate 5 highly targeted web search queries to find information about the specific target described below.

                    ## Goal
                    Find real, publicly available information about THIS specific target — not generic results about the topic area.

                    ## Rules
                        - Focus queries entirely on the specific target (name, username, domain, IP, email, etc.)
                        - Use exact match quotes around names/usernames to avoid unrelated results
                        - Cover different intelligence angles:
                            - social media profiles
                            - code repositories (GitHub, GitLab, etc.)
                            - mentions (news, blogs, forums)
                            - leaked data / breaches
                            - public records / documents
                        - Use advanced operators when useful:
                            - site:
                            - inurl:
                            - intitle:
                            - filetype:
                        - Prioritize precision over volume
                        - Avoid broad or generic queries

                    ## Output format
                        ["query 1", "query 2", "query 3", "query 4", "query 5"]

                    ## STRICT
                        - Output ONLY a JSON array
                        - No explanations
                        - No markdown
                        - No ``` or formatting wrappers
                        - No extra text before or after

                    ## Target
                        {ch_sketch}
                """