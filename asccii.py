import requests
from bs4 import BeautifulSoup
import os

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
ascii = """

                       _                                _   
    /\                (_)                              | |  
   /  \   ___  ___ ___ _  __ _  ___ _ __   ___ _ __ ___| |_ 
  / /\ \ / __|/ __/ __| |/ _` |/ _ \ '_ \ / _ \ '__/ _ \ __|
 / ____ \\__ \ (_| (__| | (_| |  __/ | | |  __/ | |  __/ |_ 
/_/    \_\___/\___\___|_|\__, |\___|_| |_|\___|_|  \___|\__|
                          __/ |                             
                         |___/                              
bynorahmad           

"""
print (ascii)
data = input("Masukkkan kata : ")
r = requests.post("https://www.kammerl.de/ascii/AsciiSignature.php", data={'figlettext':data})
soup = BeautifulSoup(r.text, 'html.parser')

res = soup.find('small')

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
print(res.text)
print('Sukses mamank tinggal kopi aja coded by Nor Gans Tq:v')
