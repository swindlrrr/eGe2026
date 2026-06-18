from ipaddress import ip_network
net = ip_network(f'146.180.173.153/255.192.0.0', 0)
print(net[-2])
