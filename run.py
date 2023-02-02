import os, time
from os import system as sis
from time import sleep as turu
from os import mkdir as dor
try:sis("git pull")
except:pass
try:dor("RESULTS")
except:pass
try:dor("DATA")
except:pass

def memek():
    sis('clear')
    print("Tools ini free to used, hasil tidak maksimal jangan mengeluh, hargai codder.")
    susu_nahida = input(f" Apakah anda mengerti? : ")
    if susu_nahida in ["y","Y","Ya","YA"]:
       open('DATA/alert.json','w').write('tools by ikz')
       turu(2);print('Tools telah dihapus, terimakasih atas waktunya menjadi kelinci percobaan')
       #import main
    elif susu_nahida in ["t","T","tidak","Tidak","TIDAK"]:
         print("Bye!!!")
         turu(3);exit()
    else:
         print("Yang bener ajg")
         turu(2);memek()

def kontol():
    try:open('DATA/alert.json','r').read()
    except FileNotFoundError:memek()
    print('Tools telah dihapus, terimakasih atas waktunya menjadi kelinci percobaan')
    #import main

kontol()
#(:)kontol.
