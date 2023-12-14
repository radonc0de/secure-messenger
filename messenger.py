import socket
import threading
import sys
import time
from diffie_hellman import DiffieHellman

def tcp_server(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen()
	print(f"Server listening on {host}:{port}")

	conn, addr = sock.accept()
	with conn:
		print(f"\nConnected by {addr}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(f"\nReceived: {data.decode()}\nEnter message:", end='')

def tcp_client(server_host, server_port):
	dh_secret = 0
	print("Starting Client")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		disconnected = True
		while disconnected:
			try:
				sock.connect((server_host, server_port))
				disconnected = False;
			except ConnectionRefusedError:
				time.sleep(1)

		while True:
			message = input("Enter message:")
			if message.lower() == 'exit':
				break
			elif message.lower() == 'dh':
				print("Initiating Diffie-Hellman Algorithm")
				message = "DH"
			sock.sendall(message.encode())

if __name__ == "__main__":
	if len(sys.argv) == 5:
		print("Valid Inputs. Intializing Client/Server...")
		client_ip = sys.argv[1]
		client_port = sys.argv[2]
		server_ip = sys.argv[3]
		server_port = sys.argv[4]

		print("Initializing Server...")	
		server_thread = threading.Thread(target=tcp_server, args=(client_ip, int(client_port)))
		server_thread.start()
		print("Server Initialized.")

		time.sleep(1)

		print("Initializing Client...")
		tcp_client(server_ip, int(server_port))

		#client_thread = threading.Thread(target=tcp_client(server_host=server_ip))
		#client_thread.start()

		server_thread.join()
		#client_thread.join()
