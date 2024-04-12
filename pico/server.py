import network
import socket             # set up a data connection with the client
from machine import Pin   # pinout interface

# init access point ====================================================================
serverName = 'Drone Brain'
password = 'mobile24'
ap = network.WLAN(network.AP_IF)                      	# create an access point network
ap.config(essid=serverName, password=password)        	# set name and 
ap.active(True)
print('Successfuly created network: %s' % serverName)
print(ap.ifconfig())
# ======================================================================================

# init led pins
rled = machine.Pin(14, Pin.OUT)
bled = machine.Pin(15, Pin.OUT)
                                    
# create a socket interface ============================================================
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# creating socket object
sock.bind(('', 800)) 	# bind (connect) sock to port 800 on this pico's ip address
sock.listen(1)			# (the first value returned from ap.ifconfig())
# ======================================================================================

conn, addr = sock.accept() 			
print('Got a connection from %s' % str(addr))
    
while True:
    # recieve data from the socket
    request = conn.recv(1024)        
    if request == b'':
        break
    print('Content = %s' % request)
        
# cleanup
conn.close()
sock.close()
ap.active(False)
print("Exit Successful")