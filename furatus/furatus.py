import requests
from bs4 import BeautifulSoup
import os

class Furatus:
    def __init__(self):
        self._headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

    def _request(self, url: str, proxies: dict = None) -> requests.Response:
        res = requests.get(url, headers=self._headers)
        return res


    def _get_img_src(self, url: str) -> str | None:
        # get html of webpage
        html = self._request(url).text
        if html:
            # get img tag from html
            soup = BeautifulSoup(html, 'html.parser')
            for tag in soup.find_all("img"):
                if "image.prntscr.com" in tag["src"] or "i.imgur.com" in tag["src"]:
                    return tag["src"]


    def _dl_img_from_url(self, url: str, output: str, filename: str) -> bool:
        res = self._request(url)
        if res.status_code == 200:
            if not os.path.isdir(output):
                os.makedirs(output)
            with open(os.path.join(output, filename), "wb") as f:
                f.write(res.content)
                return True
        else:
            return False


    def build_url(self, code):
        return f"https://prnt.sc/{code}"


    def download(self, url, output, filename) -> bool:
        src = self._get_img_src(url)
        if src:
            success = self._dl_img_from_url(src, output, filename)
            return success
        else:
            return False