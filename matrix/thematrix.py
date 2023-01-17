#modules
from os import name, system
import colorama
import time
import sys


#clear function
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

#slow typing function
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(9./90)

clear()
time.sleep(3)
text = ('\033[92m'+ "Wake up, Neo...")
sprint(text)
time.sleep(3)
clear()
text = ('\033[92m'+ "The Matrix has you...")
sprint(text)
time.sleep(3)
clear()
text = ('\033[92m'+ "Follow the white rabbit.")
sprint(text)
time.sleep(3)
clear()
text = ('\033[92m'+ "Knock, knock, Neo.")
sprint(text)
time.sleep(3)





















