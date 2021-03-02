#!/usr/bin/env python3

# AJ2K

import argparse
from pwn import *

# ~~~~~~~~~~~~~~~~~ INIT

parser = argparse.ArgumentParser(description='Welcome :)')
requiredNamed = parser.add_argument_group('Required Arguments')
requiredNamed.add_argument("-u", dest="URL",  help="host eg 192.168.0.50", required=True)
args = parser.parse_args()

def error():
     parser.print_help()
     quit()

try:
     Host = args.URL
except:
     error()

r = remote(Host, 1337)
time.sleep(1)

# ~~~~~~~~~~~~~~~~~ GET STARTING TEXT

header = r.recvuntil("Answer my questions 1000 times and I'll give you your gift.\n")
loop = 0

# ~~~~~~~~~~~~~~~~~ ANSWER 1000 maths questions to 1dp

while loop <= 1000:

     #print(header)
     #print(questionRaw)

     questionRaw = r.recvline()
     questionStripped = questionRaw.decode().replace('(', '').replace(')', '').replace(',', '').replace('> ', '').replace('\n', '').replace("'", '')

     answer = str(eval(questionStripped))
     answer = float(answer)
     answer = round(answer,1)

     print(questionStripped + " = " + str(answer))

     r.sendline(str(answer))

     #questionRaw = r.recvline()
     #print(questionRaw)
     loop += 1

# ~~~~~~~~~~~~~~~~~ GET VICTORY SECRET

print("\n" + r.recvline().decode())
r.recvline()
print(r.recvline().decode())