import requests
from bs4 import BeautifulSoup

url_file = open('urls.txt', 'r')
removed = 0
not_found = 0
for url in url_file:
    if 'blogspot' in url:
        res = requests.get(url)
        try:
            soup = BeautifulSoup(res.text, 'lxml')
            h1 = soup.find('h1').text.lower()
            print("[+]", url)
            if 'blog not found' in h1:
                print(":", "Blog Not Found!")
                not_found += 1
                with open('not_found.txt', 'a') as file:
                    file.write(url + '\n')
            elif 'blog has been removed' in h1:
                print(":", "Blog Removed!")
                removed += 1
                with open('removed.txt', 'a') as file:
                    file.write(url + '\n')
        except:
            if res.status_code == 404:
                print("Blog or site is removed!")
                removed += 1
                with open('removed.txt', 'a') as file:
                    file.write(url + '\n')

print("====Done====")
print("Not found:", not_found)
print("Removed:", removed)