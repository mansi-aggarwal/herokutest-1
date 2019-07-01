import socket

HOST = '127.0.0.1'
PORT = 54321
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Listen for incoming connections')
s.listen(1)
while True:
    conn, addr = s.accept()
    print ('Client connected with ' , addr)
    data = conn.recv(BUFFER_SIZE)
    if data:
        print('Client to Server: ' , data)
        conn.send(data.upper())
conn.close()
