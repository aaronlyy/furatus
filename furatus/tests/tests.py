# tests.py

import lightshot

test_url: str = "https://prnt.sc/bch5cv"
removed_url: str = "https://prnt.sc/bch5"
fail_url = "https://prnt.sc/0iz1ds"

# test _request_with_ua
# ---
res = _request_with_ua(test_url)
if res.status_code == 200:
    print(res.content)
else:
    print(res.status_code)
# ---

# test _get_source_attr
# ---
res = _request_with_ua(fail_url)
if res.status_code == 200:
    html = res.text
    src = _get_source_attr(html)
    if src:
        print(src)
    else:
        print(src)
else:
    print(res.status_code)
# ---

# test _save_content_b
# ---
res = _request_with_ua(test_url)
if res.status_code == 200:
    html = res.content
    src = _get_element_by_id(html)
    c_res = _request_with_ua(src)
    if c_res.status_code == 200:
        content = c_res.content
        success = _save_content_b(content, "folder", "file.png")
        if success:
            print("File saved!")
        else:
            print("Error saving file!")
else:
    print(res.status_code)
# ---

# test _build_url
# ---
print(_build_url(12345))
# ---

# test download
# ---
success = download(test_url, "images", "1234.png")
if success:
    print("File downloaded!")
else:
    print("Error downloading file!")
# ---