import getpass
import sys
import telnetlib
import subprocess

HOST = "192.168.122.3"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("Letmein99\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 1\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
tn.write("router ospf 1\n")
tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("end\n")
tn.write("terminal length 0\n")
tn.write("show running-config\n")

tn.write("exit\n")

print tn.read_all()
