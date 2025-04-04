import json, random, time, httpx, sys, os
from concurrent.futures import ThreadPoolExecutor
import threading
from colorama import Fore, Style
from time import strftime, localtime

sent, errored = 0, 0

# Config Load
with open("config.json") as config:
   data = json.load(config)
   delay = data["delay"]
   lastData = data["lastData"]
   lastCount = data["lastCount"]

def saveData(key, value):
   with open("config.json", "r+") as file:
     data = json.load(file)
     data[key] = value
     file.seek(0)
     json.dump(data, file, indent=2)
     file.truncate()

class Console:
   @staticmethod
   def Logger(content: str, status: bool) -> None:
     lock = threading.Lock()
     green = "[" + Fore.GREEN + Style.BRIGHT + "+" + Style.RESET_ALL + "] "
     red = "[" + Fore.RED + Style.BRIGHT + "-" + Style.RESET_ALL + "] "
     yellow = "[" + Fore.YELLOW + Style.BRIGHT + "!" + Style.RESET_ALL + "] "
     with lock:
       if status == "g":
         sys.stdout.write(f'{green}{content}\n')
       elif status == "r":
         sys.stdout.write(f'{red}{content}\n')
       elif status == "y":
         sys.stdout.write(f'{yellow}{content}\n')
   @staticmethod
   def clear() -> None:
     os.system("cls" if os.name == "nt" else "clear")

def main(data):
   global errored, sent
   headers = {
    "Authority": "chithi.me",
    "Method": "GET",
    "Path": "/",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Referer": "https://www.google.com/",
    "Sec-Ch-Ua": '"Chromium";v="121", "Not(A:Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

   Client = httpx.Client(headers=headers, timeout=60)
   try:
     postresp = Client.post("https://chithi.pockethost.io/api/chithi/letters",data={"data":data})
     if postresp.status_code == 201:
       sent += 1
       Console.Logger(f"Sent: {sent} | Errored: {errored}", status="g")
     elif postresp.status_code == 429:
       errored += 1
       Console.Logger("IP is rate limited", status="r")
     else:
       errored += 1
       try:
         message = postresp.json().get("message", "Error")
       except ValueError:
         message = postresp.text 
       Console.Logger(f"{message} {postresp.status_code}", status="r")
   except Exception as e:
     errored += 1
     Console.Logger(f"Error: {e}", status="y")

def Main():
   Console.clear()
   from colorama import Fore, Style
   print(
    Fore.CYAN + f"{'Chithi.me Spammer':>20}" +
    Fore.MAGENTA + r"""
  ______   __        __    __      __        __ 
 /      \ /  |      /  |  /  |    /  |      /  |
/$$$$$$  |$$ |____  $$/  _$$ |_   $$ |____  $$/ 
$$ |  $$/ $$      \ /  |/ $$   |  $$      \ /  |
$$ |      $$$$$$$  |$$ |$$$$$$/   $$$$$$$  |$$ |
$$ |   __ $$ |  $$ |$$ |  $$ | __ $$ |  $$ |$$ |
$$ \__/  |$$ |  $$ |$$ |  $$ |/  |$$ |  $$ |$$ |
$$    $$/ $$ |  $$ |$$ |  $$  $$/ $$ |  $$ |$$ |
 $$$$$$/  $$/   $$/ $$/    $$$$/  $$/   $$/ $$/ 
""" +
    Fore.YELLOW + "Created by Brainless Dip\n" +  # Highlight creator in yellow
    f"Current delay: {delay}\n" +
    Fore.CYAN + "Change the delay from config.json\n" +  # Change delay info in cyan
    Style.RESET_ALL  # Reset color and style at the end
)
   Console.Logger("Copy the data from network tab", status="y")
   print()
   while True:
    data = input(f"[~] Enter data {Fore.GREEN}({lastData[:15] if lastData else 'None'}){Style.RESET_ALL}: ").strip()
    if data:
       saveData("lastData",data)
       break
    elif not data and lastData:
      data = lastData
      break
    Console.Logger("Data cannot be empty. Please enter a valid data", status="y")
   while True:
     messagecount = input(f"[~] Enter message count {Fore.GREEN}({lastCount}){Style.RESET_ALL}: ")
     if messagecount.isdigit():
       messagecount = max(int(messagecount),1)
       saveData("lastCount", messagecount)
       break
     elif not messagecount:
       messagecount = int(lastCount)
       break
     else:
       Console.Logger("Invalid input. Please enter a valid integer", status="y")
   print()
   with ThreadPoolExecutor(max_workers=messagecount) as executor:
     for x in range(messagecount):
       executor.submit(main, data)
       time.sleep(delay)
   print()
   Console.Logger(f"Sent {sent} messages | {errored} Errored messages", status="y")

if __name__ == "__main__":
   Main()