import getpass
import sys
import telnetlib
import os
import csv
import subprocess

user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open('hosts.csv','r')
reader = csv.reader(f)

for row in reader:
	if row[0] == "ip_address":
		pass
	else:
		print("Ping {}..".format(row[0]))
		ping_response = os.system("ping -c 3 " + row[0] + " > /dev/null 2>&1")
		if ping_response == 0:
			print("{} HIDUP".format(row[1]))
			print("Ambil Configurasi ..{}".format(row[1]))
			HOST = row[0]
			tn = telnetlib.Telnet(HOST)
    			tn.read_until("Switch login: ")
    			tn.write(user + "\n")
    			if password:
        			tn.read_until("Password: ")
        			tn.write(password + "\n")
        		tn.write("enable\n")
    			tn.write("terminal length 0\n")
    			tn.write("show running-config\n")
    			tn.write("exit\n")
    			tn.write("exit\n")

    			readoutput = tn.read_all()
    			saveoutput = open(HOST + "_" + row[1] + "_show-running", "w")
    			saveoutput.write(readoutput)
    			saveoutput.close

f.close()
