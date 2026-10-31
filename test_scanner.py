import socket
target_ip= '10.85.47.176'
port = range(1, 1025) 
for ports in port:

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	result= s.connect_ex((target_ip, ports))
	if result ==0:
		print(f'port {ports} is open')
	
	s.close()
