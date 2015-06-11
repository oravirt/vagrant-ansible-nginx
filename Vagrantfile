# -*- mode: ruby -*-
# # vi: set ft=ruby :
 
VAGRANTFILE_API_VERSION = "2"
 
# We need yaml to read the hosts.yml file
require 'yaml'
 
# Read YAML file with box details
servers = YAML.load_file('hosts.yml')

# Create inventory file for Ansible by reading the hosts.yml file (ugly, but I dont know ruby...)
require "fileutils"
f = File.open("inventory","w")
servers.each do |servers|
 f.puts servers["group"]
 f.puts servers["name"] + "  ansible_ssh_host=" + servers["ip"] + "  ansible_ssh_user=vagrant " + " ansible_ssh_private_key_file=" + servers["private_key"]
end # servers.each
f.close

# Create VM's
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.ssh.insert_key = false
 
  # Loop through hosts.yml to build VM's
  servers.each do |servers|
    config.vm.define servers["name"] do |srv|
      srv.vm.box = servers["box"]
      srv.vm.hostname = servers["name"]
      srv.vm.network "private_network", ip: servers["ip"]
      srv.vm.provider :virtualbox do |vb|
        vb.name = servers["name"]
        vb.memory = servers["ram"]
      end
    end
  end
# This is the provisioning step performed by Ansible. Uncomment if it should be run as part of vagrant up
# Since the way the provisioning works with multiple machines, its faster to run the provisioning step manually after the machines are built
#
#  config.vm.provision "ansible" do |ansible|
#    ansible.playbook = "lb-nginx.yml"
#    ansible.limit = "all"
#    ansible.groups = {
#        "loadbalancer" => ["lb"],
#         "webservers" => ["web1", "web2","web3"],
#         "all_groups:children" => ["loadbalancer", "webservers"]
#        }
#  end

end
