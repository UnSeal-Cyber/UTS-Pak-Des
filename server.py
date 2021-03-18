import socket
import threading




HEADER = 64
#header untuk menentukan banyak bytes pesan


#port 5050 mksudnya port yang kosong
PORT = 5050

#masukkan IP Addres internet/wifi
#SERVER = "192.168.1.108"
#socket.gethostbyname(socket.gethostbyname()) mksudnya otomatis masukkan IP Adress
SERVER = socket.gethostbyname(socket.gethostname())


#ADDR adalah address untuk menghubungkan server dengan port
ADDR = (SERVER, PORT)

FORMAT = 'utf-8'
#format encoding

DISCONNECT_MESSAGE = "!DISCONNECT"
#untuk menutup koneksi dari client


# intuk lihat / cek isis SERVER : 
# print(server)

#socket.AF_INET membuat tipe socket menjadi internet / tipe inet yang mau kita lihat
#socket.SOCK_STREAM meliht data melalui socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)






def handle_client(conn, addr):
    #conn artinya connection
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected :
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            #menerima pesan dari socket conn
            #mendecode kembali pesannya
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}]{msg}")
            #memunculkan pesan dari address tertentu
            conn.send("Msg recieved".encode(FORMAT))
            #meng encode pesan yang dikirimkan ke kita

    conn.close()

def start():
    server.listen()
    #listen artinya menunggu koneksi utk setup
    print(F"[LISTENING] Server is listening on {SERVER}")
    print(F"============================================")
    print( "==========type 'end' to disconnect==========")
    while True:
        conn, addr = server.accept()
        #menerima informasi seperti IP dan PORT dan mengirim informasi address ke conn
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        #membuat thread untuk memasingkan informasi pada args yaitu conn dan addr ke target handle_client 
        thread.start()
        #menjalankan thread yang telah dibuat
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
        #untuk melihat coneksi yang aktif 


print("[STARTING] server is starting...")
start()





