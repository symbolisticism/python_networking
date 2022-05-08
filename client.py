import socket
import PySimpleGUI as sg

# PySimpleGUI code is from https://pysimplegui.readthedocs.io/en/latest/
sg.theme('DefaultNoMoreNagging') # add a color theme to the GUI
layout = [ # this is the content inside the GUI window
  [sg.Text("Enter the IP address of the computer you'd like to send a message to: "), sg.InputText()],
  [sg.Text("Enter the message you'd like to send: "), sg.InputText()],
  [sg.Button('Send'), sg.Button('Cancel')]
]

# create the window
window = sg.Window('A System for Computer Communication', layout)

# event loop to process events and get the values of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
  print(f'You entered: "{values[0]}" and "{values[1]}"')

window.close()

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = values[0];
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)
  print(client.recv(2048).decode(FORMAT))

# sends a message to the server
send(values[1])
# waits for input from the server side before it 
#   transmits the next message
input()
send("Pretty cool that you can send your own message over the network, right?")
input()
send("Goodbye for now!")

# disconnect from the server
send(DISCONNECT_MESSAGE)