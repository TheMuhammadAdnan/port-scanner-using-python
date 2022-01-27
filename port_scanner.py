""" 

Simple Port scanner

Credit: Adnan

Ref: https://pk.linkedin.com/in/adnan-django-python

"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input(

    """socket.gethostbyname expects a host name and not an URL.

You must give www.osjajinci.com instead of http://www.osjajinci.com/

Enter host or IP Address:"""

        )

def pscan(port):

	return s.connect_ex((target,port))

for x in range(2000):

	print("Scanning Port: ", x)

	if pscan(x) == 0:

		print("Port", x," is open!")
