VERSION = "1.0.2"

IS_NEW = False

LLM_PROVIDER = ""         
LLM_API_KEY = ""
LLM_MODEL = "gemini-2.5-flash"   
LLM_MAX_TOKENS = 4096
LLM_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


SCAN_TIMEOUT = 5                    
MAX_THREADS = 10                    


USER_AGENTS_PATH = "phoenix/data/useragents.txt"
PROXIES_PATH = "phoenix/data/proxies.txt"

MAX_CRAWL_DEPTH = 2
MAX_CRAWL_PAGES = 50


REPORT_OUTPUT_DIR = "generated"
REPORT_FORMAT = "markdown"         
REPORT_INCLUDE_RAW_DATA = False     


PERSIST_STORAGE = False            
STORAGE_OUTPUT_DIR = "output/"


WHOIS_TIMEOUT = 10
SOCIAL_MEDIA_PLATFORMS = ["twitter", "linkedin", "github"]