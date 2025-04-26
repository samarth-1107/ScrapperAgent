from playwright.async_api import async_playwright

class WebScrapper:
    def __init__(self):
        self.browser = None
        self.playwright = None
        self.page = None

    async def init_browser(self):
        self.browser = await async_playwright().start
        self.playwright = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        