# lightshot.py
import requests
import os
from bs4 import BeautifulSoup as bs

def _request_with_ua(url: str, ua: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36") -> requests.Response:
    """Sends GET request to given URL with a User-Agent, defauls to Chrome"""
    headers: dict = {"User-Agent": ua}
    res: requests.Response = requests.get(url, headers=headers)
    return res

def _get_source_attr(html: str) -> str | None:
    """Gets the source attribute of the screenshot img tag"""
    soup = bs(html, "html.parser")
    img_tag: bs4.element.Tag = soup.find(id="screenshot-image")
    if img_tag:
        attr_src = img_tag["src"]
        if attr_src.startswith("https"):
            return attr_src
        else:
            return None
    else:
        return None

def _save_content_b(content: str, out_path: str, out_file: str) -> bool:
    """Saves givent content to file (write binary)"""
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    if not os.path.exists(os.path.join(out_path, out_file)):
        with open(os.path.join(out_path, out_file), "wb") as f:
            f.write(content)
        return True
    else:
        return False

def _build_url(code: str) -> str:
    """adds code to prnt.sc base url"""
    url: str = f"https://prnt.sc/{code}"
    return url

def download(url_or_code: str, out_path: str, out_file) -> bool:
    """Downloads picture from given prnt.sc link"""
    if not url_or_code.startswith("https://prnt.sc/"):
        url = _build_url(url_or_code)
    else:
        url = url_or_code
    # Get source attr from image tag
    html_res = _request_with_ua(url) # request the html of given url
    if html_res.status_code == 200:
        html = html_res.text
        attr_src = _get_source_attr(html) # get the src attribute from the screenshot img tag
        if attr_src:
            content_res = _request_with_ua(attr_src)
            if content_res.status_code == 200:
                content = content_res.content
                success_save = _save_content_b(content, out_path, out_file) # save file
                if success_save:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    # test_url: str = "https://prnt.sc/bch5cv"
    # removed_url: str = "https://prnt.sc/bch5"
    # fail_url = "https://prnt.sc/0iz1ds"

    # test _request_with_ua
    # ---
    # res = _request_with_ua(test_url)
    # if res.status_code == 200:
    #     print(res.content)
    # else:
    #     print(res.status_code)
    # ---

    # test _get_source_attr
    # ---
    # res = _request_with_ua(fail_url)
    # if res.status_code == 200:
    #     html = res.text
    #     src = _get_source_attr(html)
    #     if src:
    #         print(src)
    #     else:
    #         print(src)
    # else:
    #     print(res.status_code)
    # ---

    # test _save_content_b
    # ---
    # res = _request_with_ua(test_url)
    # if res.status_code == 200:
    #     html = res.content
    #     src = _get_element_by_id(html)
    #     c_res = _request_with_ua(src)
    #     if c_res.status_code == 200:
    #         content = c_res.content
    #         success = _save_content_b(content, "folder", "file.png")
    #         if success:
    #             print("File saved!")
    #         else:
    #             print("Error saving file!")
    # else:
    #     print(res.status_code)
    # ---

    # test _build_url
    # ---
    # print(_build_url(12345))
    # ---

    # test download
    # ---
    # success = download(test_url, "images", "1234.png")
    # if success:
    #     print("File downloaded!")
    # else:
    #     print("Error downloading file!")
    # ---
    
    pass