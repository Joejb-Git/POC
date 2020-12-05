import requests
import sys

url = sys.argv[1]
fullUrl = url + "/about/index.php?fmodule=7"
print(fullUrl)

res = requests.get(url=fullUrl)

if (not res.text) and (res.status_code == 200):
    print('vulnerable!')