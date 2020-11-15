
import socket 

host="localhost"
port=13000

socketClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

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


    message =input("Zgjedhni opsionet: ")
    socketClient.sendto(message.encode(),(host,port))
    if message.startswith("perfundo"):
        exit()

    informata=socketClient.recv(128)
    print(informata.decode())

socketClient.close()