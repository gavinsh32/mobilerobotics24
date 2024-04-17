# client.py

import socket
import sys

def main():
	if len(sys.argv) == 1:
		print("To run this program: client.py xxx.xxx.x.x")
		exit()
	else: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((sys.argv[1], 800))
		sock.sendall(b'hello, pico!')
		sock.sendall(b'hello, pico!')
		sock.sendall(b'hello, pico!')
		sock.close()

if __name__ == '__main__':
	main()