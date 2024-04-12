# client.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.4.1', 800))

def main():
	sock.sendall('hello, pico!'.encode())
	sock.sendall('hello, pico!'.encode())
	sock.sendall('hello, pico!'.encode())
	sock.close()

if __name__ == '__main__':
	main()