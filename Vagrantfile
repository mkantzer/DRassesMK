# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  # enable private network to VM
  config.vm.network "private_network", ip: "192.168.33.10"
  # Install Ansible on Vagrant Guest
  config.vm.provision "shell", inline: "sudo apt-get install software-properties-common"
  # Use correct PPA 
  config.vm.provision "shell", inline: "sudo apt-add-repository ppa:ansible/ansible -y"
  config.vm.provision "shell", inline: "sudo apt-get update"
  config.vm.provision "shell", inline: "sudo apt-get install ansible -y"
  config.vm.provision "shell", inline: "ansible --version"

  #execute anible playbook for Flask and mongoDB setup
  config.vm.provision "ansible_local" do |ansible|
 	ansible.playbook = "master.yml"
  end

end