import socket

host = "localhost"
port = 13000
klienti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klienti.connect((host,port))


print ("Zgjedhni opsionet :")
print ("IPAdresa, NumriIPortit, Reverse, Palindrome, Count, Time, Game, GCF, Convert\n")

print ("Lista e parametrave convert jane:\n"
+"cmToFeet\n"
+"FeetToCm \n"
+"kmToMiles \n"
+"MileToKm  \n")
print ("Metodat shtese ")
print ("Viti, Prime")
print( "PERFUNDO per te shkeputur lidhjen \n")


while True:
    message = input("Zgjedh nje nga opsionet: ")
    klienti.send(message.encode("UTF-8"))
     
    while True:
        modifiedMessage = klienti.recv(1024)
        mesazhi = modifiedMessage.decode("UTF-8")
        
        
        if message.startswith("PERFUNDO") or message.startswith("perfundo"):
             exit()
        else:
             print (modifiedMessage.decode("UTF-8"))
             break

             
klienti.close()