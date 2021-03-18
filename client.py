import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #mengubah int menjadi string agar bisa menghitung jumlah byte
    send_length += b' ' *(HEADER - len(send_length))
    #mengurangi header dengan panjaang msg lalu dikalikan dengan sendlength
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
        

lagi = True
while lagi :
    x = input()
    if x == "end":
        lagi = False
        send(DISCONNECT_MESSAGE) 
    else:
        send(x);

