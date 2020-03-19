import paramiko

ip = '192.168.122.2'
username = 'admin'
password = 'admin123'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password, allow_agent=False, look_for_keys=False)

for host in ip:
	ssh_client.connect(hostname=ip, username=username, password=password, allow_agent=False, look_for_keys=False)
	stdin,stdout,stderr = ssh_client.exec_command("ip address add address=172.168.2.1/24 interface=ether2") #seting ip address interface untuk hotspot
	stdin,stdout,stderr = ssh_client.exec_command("ip pool add name=dhcp_hotspot ranges=172.168.2.2-172.168.2.254") #bikin pool untuk dhcp server
	stdin,stdout,stderr = ssh_client.exec_command("ip dhcp-server add address-pool=dhcp_hotspot disabled=no interface=ether2 name=hotspot") #bikin dhcp-server pake pool yang sebelumnya dibuat
	stdin,stdout,stderr = ssh_client.exec_command("ip dhcp-server network add address=172.168.2.0/24 dns-server=8.8.8.8 gateway=172.168.2.1") #masukin network dhcp-server kita , jangan sampai kelewat
	stdin,stdout,stderr = ssh_client.exec_command("ip hotspot profile add dns-name=fariz.net hotspot-address=172.168.2.1 name=hotspot1") # buat profile buat hotspot
	stdin,stdout,stderr = ssh_client.exec_command("ip hotspot add address-pool=dhcp_hotspot disabled=no interface=ether2 name=hotspot1 profile=hotspot1") # buat hotspot
	stdin,stdout,stderr = ssh_client.exec_command("ip hotspot user add name=fariz password=Letmein99") # create user hotspot
	stdin,stdout,stderr = ssh_client.exec_command("ip dhcp-server print")
	stdin,stdout,stderr = ssh_client.exec_command("ip hotspot print")

print((stdout.read()))