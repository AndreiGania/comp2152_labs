import platform
import socket
import os
import sys

print(f"\n Machine Type: {platform.machine()}")

print(f"\n Processor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\n Default Timeout for Socket: {socket.getdefaulttimeout()}")

print(f"\n OS Type: {os.name}")
print(f"\n OS Name: {platform.system()}")
print(f"\n Current PID: {os.getpid()}")
