
import socket 
from threading import Thread
import datetime
import random
import string
import sys
import math
import threading


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start() 
         
    
    def listenToClient(self, client, address): 
        while True : 
          try: 
            message=client.recv(1024)
            message = message.decode("UTF-8") 
            print("Te dhenat e pranuara nga klienti: ", message)   
            message=message.upper() 
            if message.strip() == "IPADRESA" :
                 response = "IP adresa e klientit eshte " + client.getpeername()[0]
                 client.send(( str(response)).encode("UTF-8"))
            elif message.strip() == "NUMRIIPORTIT":
                 response = "Klienti eshte duke perdorur portin "+ str(client.getpeername()[1])
                 client.send(( str(response)).encode("UTF-8"))
            elif message.startswith("REVERSE "):
                mesazhi = message[8:]
                if(mesazhi!=""):
                    mesazhi=''.join(reversed(mesazhi))
                    client.send(("Teksti ne reverse eshte "+str(mesazhi)).encode("UTF-8"))
                else:
                    client.send("Nuk keni shtypur tekst!".encode("UTF-8"))
            elif message.startswith("PALINDROME "):
                mesazhi = message[11:]
                if(mesazhi!=""):
                    mesazhi1=''.join(reversed(mesazhi))
                    if(mesazhi1!=mesazhi):
                        client.send("Teksti i dhene nuk eshte  palindrome ".encode("UTF-8"))
                    else:
                        client.send("Teksti i dhene eshte palindrome ".encode("UTF-8"))
                else:
                    client.send("Nuk keni shtypur tekst!".encode("UTF-8"))
            elif message.startswith("COUNT "):
                mesazhi = message[6:]
                if(mesazhi!=""):
                    h= isinstance(mesazhi,str)
                    if h == True:
                      p = count(mesazhi)
                      client.send(str(p).encode("UTF-8"))
                    else:
                        client.send("Lejohet vetem  tekst! ".encode("UTF-8"))
                else:
                    client.send("Nuk keni shtypur tekst! ".encode("UTF-8"))
            elif message.strip()=="TIME":
                mesazhi=str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p"))
                client.send(mesazhi.encode( )) 
            elif message.strip()=="GAME":
                client.send(str(random.sample(range(1, 35), 5)).encode("UTF-8"))
            elif message.startswith("CONVERT "):
                mesazhi = str(message).split(" ")
                if (mesazhi[1] != ""):
                    try:
                        if (mesazhi[2] != ""):
                            if mesazhi[1].lower() == "cmtofeet":
                                value = round(float(mesazhi[2]) / float(30.48), 3)
                                client.send(str(value).encode("UTF-8"))
                            elif mesazhi[1].lower() == "feettocm":
                                value = round(float(mesazhi[2]) * float(30.48), 3)
                                client.send(str(value).encode("UTF-8"))
                            elif mesazhi[1].lower() == "kmtomiles":
                                value = round(float(mesazhi[2]) / float(1.609), 3)
                                client.send(str(value).encode("UTF-8"))
                            elif mesazhi[1].lower() == "miletokm":
                                value = round(float(mesazhi[2]) * float(1.609), 3)
                                client.send(str(value).encode("UTF-8"))
                            else:
                                client.send("Shtypni njerin nga opsionet!".encode("UTF-8"))
                        else:
                            client.send("Shtypni numrin!".encode("UTF-8"))
                    except Exception:
                        client.send("Shtypni numrin !".encode("UTF-8"))
                elif ((mesazhi[1] == "")):
                    client.send("Shkruani njerin nga opsionet ne konvertim dhe numrin!".encode())
            elif message.startswith("VITI"):
              try:  
                mesazhi = str(message).split(" ") 
                if (mesazhi[1] != ""):
                     try:
                        if (mesazhi[2] != ""): 
                          y = mesazhi[1]
                          if int(y)% 400 == 0:
                            leap = 1
                          elif int(y) % 100 == 0:
                            leap = 0
                          elif int(y)% 4 == 0:
                            leap = 1
                          else:
                            leap = 0 
                          if leap == 1:
                              p="Viti eshte i brishte "
                          else:
                              p="Viti nuk eshte i brishte "
                          m = mesazhi[2]
                          lista = ["1","3","5","7","8","10","12"]   
                          if m in lista:
                              x= 31
                              client.send((str(p)+"\nNumri i diteve eshte:"+str(x) ).encode("UTF-8"))
                          elif m =="2":
                              x= 28 +leap
                              client.send((str(p)+"\nNumri i diteve eshte: "+str(x) ).encode("UTF-8"))     
                          else:       
                              x= 30
                              client.send((str(p)+"\nNumri i diteve eshte: "+str(x)).encode("UTF-8"))
                        else:
                              client.send("Shtypni muajin!".encode("UTF-8"))
                     except Exception:
                           client.send("Shkruani muajin !".encode("UTF-8"))
                else:
                    client.send("Shkruani vitin dhe muajin ! ".encode())
              except OSError:
                  client.close()      

            elif message.startswith("PRIME"):
                mesazhi = str(message).split(" ")
                var = prime(mesazhi[1])
                client.send(str(var).encode("UTF-8"))
            elif message.startswith("GCF"):
                    mesazhi = str(message).split(" ")
                    if (mesazhi[1] != ""):
                        if (mesazhi[2] != ""): 
                            x=int(mesazhi[1])
                            y=int(mesazhi[2])
                            f=math.gcd(x, y)
                            client.send(("GCF i "+str(x)+" dhe "+str(y) +" eshte: " +str(f)).encode("UTF-8"))
                        else:
                            client.send("Shkruani dy numra !".encode("UTF-8"))
                    else:
                        client.send("Shkruani numrat !".encode("UTF-8"))
                           
            else:  
                client.send("Ju lutem shenoni njerat nga kerkesat!".encode())
          except OSError:
              client.close()


def prime(n):
    if (int(n)==1):
        return False
    elif (int(n)==2):
        return True
    else:
        for x in range(2,int(n)):
            if(int(n) % x==0):
                return False
        return True
def count(s):
        fjala1 = s.replace(" ", "")
        fjala1=list(str(fjala1))
        zanore=0
        bashketingllore=0
        for i in fjala1:
            if i in ["A", "E", "Y", "U", "I", "O"]:
                 zanore+=1
            else:
                 bashketingllore+=1 
        return ("Numri i bashketingelloreve eshte " + str(bashketingllore)+" ndersa numri i zanoreve eshte " 
                       + str(zanore) )                      
 


port = 13000
print ("Serveri eshte ne pritje te kerkesave") 
ThreadedServer('',port).listen()

















