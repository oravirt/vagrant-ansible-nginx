<b> What? </b>

This vagrantfile (using Virtualbox) creates any number of nginx web-nodes and can provision them using the playbook lb-nginx.yml. By default it will create 3 web nodes and they are fronted by a loadbalancer (also running nginx).
If you want to add a new web node, just alter the hosts.yml file to create an extra node, run 'vagrant up' and then the playbook and it is in use.

The provisioning step has been commented out from the Vagrantfile, since it will run for every machine that gets created. So, it is faster to run the playbook manually after the VM's are created.
The inventory file is built everytime you run 'vagrant up'. The inventory works but is really ugly, but I dont know ruby, so there.

There is also a small python script (lbtest.py) that makes a configurable number of requests to the loadbalancer to see if the traffic gets balanced properly.

As the playbook is using the Vagrant insecure_private_key, the path should be changed in the hosts.yml file. It is hardcoded to my environment.

Ansible Role Name
=================

nginx - Installs and configures an n-node web cluster fronted by a loadbalancer

Example Playbook
----------------
To run the playbook, execute the 'run-ansible-playbook.sh' script and pass in the playbook.

./run-ansible-playbook.sh lb-nginx.yml


To test if loadbalancing is working, run the lbtest.py script:

./lbtest.py -u http://192.168.9.90 -r 300

License
-------

MIT

Author Information
------------------

Mikael Sandstrom, oravirt@gmail.com
