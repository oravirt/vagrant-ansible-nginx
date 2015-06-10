#!/usr/bin/env python
from urllib2 import urlopen
from collections import Counter

output = []
for i in range(1,301):
	response = urlopen ('http://192.168.9.90')
	host = response.read()
        host = host.rstrip('\n')
        output.append(host)
	
counted_output = Counter(output)
print
print "Making sure loadbalancing is working. Should get an even number of hits on each node"
print
for host in sorted(counted_output):
	print host, counted_output[host]  # Pretty printing of the list
print
