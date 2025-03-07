import platform
import socket
print(f"\n Machine Type: {platform.machine()}")

print(f"\n Processor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\n Default Timeout for Socket: {socket.getdefaulttimeout()}")
