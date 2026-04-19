from phoenix.modules.rotators.proxy_rotator import ProxyRotator
from phoenix.modules.rotators.useragent_rotator import UARotator

from playwright.sync_api import sync_playwright
import random
import time


class CrawlURL:

    def __init__(self):
        self.proxy_rotator = ProxyRotator()
        self.ua_rotator = UARotator()

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False,
            executable_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        )

        self.context = None
        self.page = None

    def _new_session(self):
        proxy = self.proxy_rotator.rotate()
        ua = self.ua_rotator.rotate()

        if self.context:
            self.context.close()

        self.context = self.browser.new_context(
            user_agent=ua,
            proxy={"server": proxy} if proxy else None,
            viewport={"width": random.randint(1200, 1400), "height": random.randint(700, 900)},
            locale="en-US"
        )

        self.page = self.context.new_page()

        self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            window.chrome = { runtime: {} };
        """)

        self.page.route("**/*", lambda route: (
            route.abort() if route.request.resource_type in ["image", "font", "media"]
            else route.continue_()
        ))


    def crawl(self, url: str):
        try:
            self._new_session()
            time.sleep(random.uniform(1.5, 3.5))

            with self.page.expect_response(
                lambda r: "web_profile_info" in r.url,
                timeout=20000  # explicit timeout, default is only 30s but good to be explicit
            ) as resp:
                self.page.goto(url, timeout=15000, wait_until="domcontentloaded")

            response = resp.value
            data = response.json()
            return data

        except Exception as e:
            print(f"[crawl error] {type(e).__name__}: {e}") 
            return None
        
    
    def close(self):
        if self.context:
            self.context.close()
        self.browser.close()
        self.playwright.stop()