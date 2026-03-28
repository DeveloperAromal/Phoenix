import urllib.parse
from typing import Dict


class CraftURL:
    
    def __init__(self):
        pass

    def _encode(self, username: str) -> str:
        return urllib.parse.quote(username)

    def urls(self, username: str) -> Dict[str, str]:
        u = self._encode(username)

        return {
            "google": f"https://www.google.com/search?q={u}",
            "duckduckgo": f"https://duckduckgo.com/?q={u}",
            "bing": f"https://www.bing.com/search?q={u}",
            "yandex": f"https://yandex.com/search/?text={u}",

            "twitter": f"https://twitter.com/{u}",
            "instagram": f"https://www.instagram.com/{u}",
            "facebook": f"https://www.facebook.com/{u}",
            "tiktok": f"https://www.tiktok.com/@{u}",
            "snapchat": f"https://www.snapchat.com/add/{u}",
            "pinterest": f"https://www.pinterest.com/{u}",
            "reddit": f"https://www.reddit.com/user/{u}",
            "tumblr": f"https://{u}.tumblr.com",

            "linkedin": f"https://www.linkedin.com/search/results/all/?keywords={u}",

            "github": f"https://github.com/{u}",
            "gitlab": f"https://gitlab.com/{u}",
            "bitbucket": f"https://bitbucket.org/{u}",
            "stackoverflow": f"https://stackoverflow.com/users/{u}",
            "kaggle": f"https://www.kaggle.com/{u}",
            "devto": f"https://dev.to/{u}",
            "medium": f"https://medium.com/@{u}",
            "hashnode": f"https://hashnode.com/@{u}",

            "youtube": f"https://www.youtube.com/@{u}",
            "twitch": f"https://www.twitch.tv/{u}",
            "vimeo": f"https://vimeo.com/{u}",

            "steam": f"https://steamcommunity.com/id/{u}",
            "epicgames": f"https://www.epicgames.com/id/{u}",
            "roblox": f"https://www.roblox.com/user.aspx?username={u}",

            "quora": f"https://www.quora.com/profile/{u}",
            "disqus": f"https://disqus.com/by/{u}",
            "producthunt": f"https://www.producthunt.com/@{u}",

            "soundcloud": f"https://soundcloud.com/{u}",
            "spotify": f"https://open.spotify.com/user/{u}",
            "bandcamp": f"https://{u}.bandcamp.com",

            "tinder": f"https://tinder.com/@{u}",
            "bumble": f"https://bumble.com/{u}",

            "haveibeenpwned": f"https://haveibeenpwned.com/unifiedsearch/{u}",
            "dehashed": f"https://www.dehashed.com/search?query={u}",

            "pastebin": f"https://pastebin.com/search?q={u}",
            "ghostbin": f"https://ghostbin.com/search?q={u}",
            
            "dork_social": f'https://www.google.com/search?q="{u}"+site:twitter.com OR site:instagram.com OR site:facebook.com',
            "dork_professional": f'https://www.google.com/search?q="{u}"+site:linkedin.com OR site:github.com',
            "dork_files": f'https://www.google.com/search?q="{u}"+filetype:pdf OR filetype:docx OR filetype:xlsx',
            "dork_username_exact": f'https://www.google.com/search?q="inurl:{u}"',
            "dork_email": f'https://www.google.com/search?q="{u}"+"@gmail.com"'
        }