# author : @thebhikandeshmukh
# -*- coding: utf-8 -*-                                                       bash.py
# author : LunaticTunnel
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'
os.system('clear')
banner0 = "\033[96m===============-LUNATIC-==================\033[0m"
memek = " "
banner1 = "\033[35m==========================================\033[0m"
banner2 = "\033[31mScript Sederhana\033[0m".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)
banner3 = "\033[1;32mContoh encrypt: \033[0m"
banner4 = " ( /sdcard/namafile.sh )"
banner5 = "\033[1;32mContoh Decrypt: \033[0m"
banner6 = " ( /sdcard/hasil.sh )"
banner7 = "\033[35m==========================================\033[0m"
banner8 = "\033[1;31mWARNING !!!\033[0m"
kontol = "hanya untuk file bash / sh / shell"
banner9 = " "
banner10 = """
   {}[{}1{}]{} Encript [ bash ]      {}[{}2{}]{} Decrypt [ bash ]
""".format(G,W,G,W,G,W,G,W)

print banner0
print memek
print banner1
print banner2
print banner3
print banner4
print banner5
print banner6
print banner7                                                                          
print banner8
print kontol
print banner9                                                                           
print banner10

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + C + "> " + G)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + C)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")


takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Wrong input")
