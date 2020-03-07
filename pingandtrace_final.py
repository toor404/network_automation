import csv
import os

f = open('hosts.csv','r')
reader = csv.reader(f)

for row in reader:
	if row[0] == "ip_address":
		pass
	else:
		print("Ping {}..".format(row[0]))
		ping_response = os.system("ping -c 3 " + row[0] + " > /dev/null 2>&1")
		if ping_response == 0:
			print("{} HIDUP! ".format(row[1]))
			print("\n")
		else:
			print("{} MATI!".format(row[1]))
			traceroute_response = os.system("traceroute -m 5 " + row[0])
			print("\n")	


f.close()