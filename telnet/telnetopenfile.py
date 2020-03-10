import getpass
import sys
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open ('myswitches')

for line in f:
    print "Configuring Switch " + (line)
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("enable\n")
    tn.write("Letmein99\n")
    tn.write("terminal length 0\n")
    tn.write("show running-config\n")
    tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.close

    print tn.read_all()