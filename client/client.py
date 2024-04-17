# client.py

import socket
import sys

def main():
	
	if len(sys.argv) == 2:
		# create a socket connected to Pico IP address (sys.argv[1])
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((sys.argv[1], 800))

		# send three messages
		# b indicates 'binary literal'
		# sendall splits the total data up in to
		# seperate packets if larger
		sock.sendall(b'hello, pico!')
		sock.sendall(b'hello, pico!')
		sock.sendall(b'hello, pico!')
		
		# close socket and connection
		sock.close()

	# incorrect run paramaters
	else: 
		print("To run this program: python3 client.py xxx.xxx.x.x")
		exit()

if __name__ == '__main__':
	main()