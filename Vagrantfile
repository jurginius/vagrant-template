# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provider "virtualbox" do |v|
    v.name = "pdf_maker_precise64"
    v.memory = 1024
#   v.gui = true
  end

  config.vm.box = "hashicorp/precise64"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.hostname = "augustus"

  # config.vm.network "private_network", ip: "192.168.33.10"

  # config.vm.network "public_network"

  # config.ssh.forward_agent = true

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "play.yml"
    ansible.sudo = true
  end
end
