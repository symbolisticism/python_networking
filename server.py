import socket
import threading

#define variables
HEADER             = 64
PORT               = 5050
SERVER             = socket.gethostbyname(socket.gethostname())
ADDR               = (SERVER, PORT)
FORMAT             = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# print out the IP address of the computer
print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
  # new connection message
  print(f'[NEW CONNECTION] {addr} connected.')

  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
        connected = False

      print(f"[{addr}] {msg}")
      # sends a message back to the client
      conn.send("Message received".encode(FORMAT))
  # close the connection
  conn.close()

def start():
  server.listen()
  # message showing which IP address the server is listening on
  print(f"[LISTENING] Server is listening on {SERVER}")
  while True:
    conn, addr = server.accept()
    # use multiple threads so that the computer can handle multiple
    #   items at a time rather than waiting on a response
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    # message displaying the amount of active connections
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print('[STARTING] server is starting...')
start()