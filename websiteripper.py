import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from difflib import SequenceMatcher

def findLongestSubstring(str1, str2):
    matcher = SequenceMatcher(None, str1, str2)
    match = matcher.find_longest_match(0, len(str1), 0, len(str2))
    if match.size > 0:
        return str1[match.a : match.a + match.size]
    return ""

url = "https://inter.co/"

session = requests.session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:154.0) Gecko/20100101 Firefox/154.0" #Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36

html = session.get(url).content
soup = bs(html, 'html.parser')
response = session.get(url)
print(response.status_code)

css_files = []
for css in soup.find_all("link"):
    if css.attrs.get("href"):
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)
        print(css_files)

with open('index.html', 'w') as f:
    f.write(str(soup))
i = 0
for file in css_files:
    if "css" in file:
        response = requests.get(file)
        responseContent = str(response.content)
        responseContent = responseContent.encode("utf-8").decode("unicode_escape")
        fileNameIndex = file.rfind("/")
        print(file [fileNameIndex:])
        fileStart = findLongestSubstring(file, url)
        print(fileStart)
        if ".css" in file:
            with open(f'{file [fileNameIndex+1:]}', 'w') as f:
                f.write(responseContent [2:(len(responseContent))-1])
        i += 1
    if "png" in file:
        response = requests.get(file)
        responseContent = str(response.content)
        responseContent = responseContent.encode("utf-8").decode("unicode_escape")
        fileNameIndex = file.rfind("/")
        print(file [fileNameIndex:])
        fileStart = findLongestSubstring(file, url)
        print(fileStart)
        if ".png" in file:
            with open(f'{file [fileNameIndex+1:]}', 'w') as f:
                f.write(responseContent [2:(len(responseContent))-1])
        i += 1
    if "svg" in file:
        response = requests.get(file)
        responseContent = str(response.content)
        responseContent = responseContent.encode("utf-8").decode("unicode_escape")
        fileNameIndex = file.rfind("/")
        print(file [fileNameIndex:])
        fileStart = findLongestSubstring(file, url)
        print(fileStart)
        if ".svg" in file:
            with open(f'{file [fileNameIndex+1:]}', 'w') as f:
                f.write(responseContent [2:(len(responseContent))-1])
        i += 1