#!/usr/bin/env python
from urllib2 import urlopen
from collections import Counter
import argparse


def get_args():
	parser = argparse.ArgumentParser(description='Script to see if loadblancing is working')

	parser.add_argument('-u', '--url', type=str, required = True, help="The URL to connect to")
 
	parser.add_argument('-r','--requests', type=int, required = True, help="The number of requests to make")

	args = parser.parse_args() 

	requests = args.requests
	url = args.url

	return requests, url

requests, url = get_args()
output = []	                     # Empty list

print
for i in range(0,requests):
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
