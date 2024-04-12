import network
import socket             # set up a data connection with the client
from machine import Pin   # pinout interface

serverName = 'Drone Brain'
password = 'mobile24'

rled = machine.Pin(14, Pin.OUT)
bled = machine.Pin(15, Pin.OUT)

# create a network on the pico
ap = network.WLAN(network.AP_IF)                      # create an access point network

ap.config(essid=serverName, password=password)        # set name and 
ap.active(True)                                       # turn on
print('Successfuly created network: %s' % serverName)
print(ap.ifconfig())

# create a socket interface
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
sock.bind(('', 800))
sock.listen(1)

# main loop
while True:
    conn, addr = sock.accept()
    print('Got a connection from %s' % str(addr))
    request = str(conn.recv(1024))
    print('Content = %s' % request)