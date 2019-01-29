import os
import re
import json
import base64
import requests

url = "http://ctf.alphasec.xyz:9093/"
flag = ""

s = requests.Session()
input = None

while True:
    if input == 100:
        break
    try:
        if input == None:
            r = s.get(url)
        else:
            payload = {'input': input}
            r = s.get(url, params=payload)
    except:
        continue

    cookie = r.headers['Set-Cookie']
    match = re.search(r"session=([a-zA-Z0-9]+)", cookie)
    iteration = base64.b64decode(match.group(1)+"===").decode('utf-8')

    input = json.loads(iteration)['itera']

    #print("Iteration: {}".format(input))
    #print("Code: {}".format(r.status_code))

    if "500" in r.text:
        match = re.search(r"\<h2\>(\d+)\s-", r.text)
        code = match.group(1)
        char = chr(r.status_code - int(code))
        flag += char
        print("[*] Char found: {}".format(char))

flag = re.search(r"(flag{\w+})", flag)
print("\n[!] The flag is: {}".format(flag.group(1)))
