
import socket
import sys
import threading
from _thread import *
import random
import datetime
import math 

host = "localhost"
port = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    serverSocket.bind((host,port))
    
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()

print("Serveri eshte ne pritje te kerkesave ")



def Reverse (teksti):
       mesazhi1=''.join(reversed(teksti))
       return mesazhi1
 
def Palindrome (teksti):          
    mesazhi1=''.join(reversed(teksti))
    if(mesazhi1!=teksti):
        return "Teksti i dhene nuk eshte  palindrome "                   
    else:
         return "Teksti i dhene  eshte palindrome "        

def Count(s):
        fjala1=list(str(s))
        zanore=0
        bashketingllore=0
        for i in fjala1:
            if i in ["A", "E", "Y", "U", "I", "O"]:
                 zanore+=1
            else:
                 bashketingllore+=1 
        return ("Numri i bashketingelloreve eshte " + str(bashketingllore)+" ndersa numri i zanoreve eshte " 
                       + str(zanore) ) 
def Time():
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")
    return time

def Game():
    numbers = ""
    for n in range(1,6):
        num = random.randint(1,35)
        numbers += str(num) + " "
    return numbers

def Convert(opcioni, vlera):
    opcioni=opcioni.lower()
    if opcioni == "cmtofeet":
        value = round(vlera / float(30.48), 3)
        return (str(value))
    elif opcioni == "feettocm":
        value = round(vlera * float(30.48), 3)
        return (str(value))
    elif opcioni == "kmtomiles":
        value = round(vlera / float(1.609), 3)
        return (str(value))
    elif opcioni == "miletokm":
        value = round(vlera * float(1.609), 3)
        return (str(value))
    else:
        return "Shkruani nje nga opsionet!"  

def GCF(x,y):            
        f=math.gcd(x, y)
        return f
                  
# metodat shtese
def Prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

      
def Viti(y,m):
    if y% 400 == 0:
      leap = 1
    elif y % 100 == 0:
      leap = 0
    elif y% 4 == 0:
      leap = 1
    else:
      leap = 0 

    if leap == 1:
      p="Viti eshte i brishte "
    else:
      p="Viti nuk eshte i brishte "
                              
                         
    lista = ["1","3","5","7","8","10","12"]   
    if m in lista:
        x= 31
        return ( str(p)+"\nNumri i diteve eshte:"+str(x))
    elif m ==2 :
        x= 28 +leap
        return ( str(p)+ "\nNumri i diteve eshte: "+str(x) ) 
    else:       
        x= 30
        return (str(p)+"\nNumri i diteve eshte: "+str(x))

def ClientThread(input, address):
    try:
        mesazhi = input.decode() 
        print("Te dhenat e pranuara nga klienti: "+mesazhi)
        mesazhi=mesazhi.upper()
    except socket.error:
        print("Ka ndodhur nje problem!")   


    teksti = str(mesazhi).rsplit(" ")
   
    if not mesazhi:
        return
    elif mesazhi.strip()==("IPADRESA"):
            mesazhi = "IP Adresa e klientit eshte " + str(address[0])
    elif mesazhi.strip()==("NUMRIIPORTIT"):
            mesazhi = "Klienti eshte duke perdorur portin " + str(address[1])
    elif mesazhi.startswith("COUNT"):
        mesazhi=mesazhi[6:]
        if (mesazhi!=""):
            mesazhi1 = mesazhi.replace(" ","")
            mesazhi =  str(Count(mesazhi1)) 
        else:
            mesazhi="Shkruani tekstin!"   
    elif teksti[0]=="GCF":
        if (teksti[1]!=""):
            if (teksti[2]!=""):
                x=int(teksti[1])
                y=int(teksti[2])
                mesazhi = str(GCF(x,y))
            else:
                mesazhi="Shkruani dy numra!"
        else:
            mesazhi="Shkruani numrat!"    
    elif teksti[0]=="PRIME":
        if (teksti[1]!=""):
            n=int(teksti[1])
            mesazhi=str(Prime(n))
        else:
            mesazhi="Shkruani numrin!"    
    elif mesazhi.strip()==("TIME"):
            mesazhi = Time()
    elif mesazhi.strip()==("GAME"):
        mesazhi =  Game()
    elif(teksti[0]=="PALINDROME"):
        if (teksti[1]!=""):
          mesazhi =  str(Palindrome(teksti[1]))
        else:
          mesazhi="Shkruani tekstin!"  
    elif(teksti[0]=="REVERSE"):
        if (teksti[1]!=""):
          mesazhi =  str(Reverse(teksti[1])) 
        else:
          mesazhi="Shkruani tekstin!"   
    elif(teksti[0]=="VITI"): 
        if (teksti[1]!=""):
           if (teksti[2]!=""):
             v=int(teksti[1])
             m=int(teksti[2])
             mesazhi = str(Viti(v,m))  
           else: 
              mesazhi="Shkruani muajin!"          
        else:
            mesazhi="Shkruani vitin dhe muajin!"
    elif(teksti[0]=="CONVERT"):
        if (teksti[1]!=""):
           if (teksti[2]!=""):
              vlera = float(teksti[2])
              mesazhi = str(Convert(teksti[1], vlera))
           else:
                mesazhi="Shkruani vleren!"
        else:
            mesazhi="zgjedhni opsionin!"          
    
    else:
        mesazhi="Ju lutem shenoni njerat nga kerkesat!"
    serverSocket.sendto(mesazhi.encode(),address)


while 1:

        mesazhi, address=serverSocket.recvfrom(128)
        start_new_thread(ClientThread,(mesazhi, address))
      
serverSocket.close()