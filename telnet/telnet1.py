import getpass
import sys
import telnetlib

HOST = "192.168.122.2"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("interface bridge add name=br1\n")

print tn.read_all()
