#!/usr/bin/env python
from urllib2 import urlopen
from collections import Counter


url='http://192.168.9.90'        # The URL to test
requests=301                     # Number of requests
output = []                      # Empty list

print
for i in range(1,requests):
        response = urlopen (url)     # Make the requests
        host = response.read()       # Read the response
        host = host.rstrip('\n')     # Remove new lines
        output.append(host)          # Append each response to list

counted_output = Counter(output)          # Count the number of hosts and occurrences of each host
print
print "Making sure loadbalancing is working. Should get an even number of hits on each node"
print
for host in sorted(counted_output):       # Loop through the sorted list
	print "%s: %s" % (host, counted_output[host])  # Pretty printing of the list
print
