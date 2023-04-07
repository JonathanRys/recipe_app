# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANT_HOME='/vagrant'
APP_NAME='recipe_app'

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "hashicorp/bionic64"
  config.vm.synced_folder "recipe_app/", "/Users/jonathanrys/Development/recipe_app/recipe_app"
  config.vm.define "recipe-app" do |app|
    app.vm.hostname = "recipe-app"
    app.vm.provider :virtualbox do |vb|
      vb.name = "recipe-app"
    end
  end
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # Flask
  config.vm.network "forwarded_port", guest: 5000, host: 8086, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.56.50"
  config.vm.network :private_network, ip: "192.168.56.50"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # reboot the machine after provisioning to apply any updates and verify recovery
  config.trigger.after [:provision] do |t|
    t.name = "Reboot after provisioning"
    t.run = { :inline => "vagrant reload" }
  end
  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.synced_folder "recipe_app/", "/var/www/app"
  # build the server
  config.vm.provision "shell", path: "./scripts/build.sh", env: {
    "APP_NAME" => APP_NAME,
    "VAGRANT_HOME" => VAGRANT_HOME
  }
  # NPM should never be run as root
  config.vm.provision "shell", path: "./scripts/build_dependencies.sh", privileged: false, env: {
    "APP_NAME" => APP_NAME,
    "VAGRANT_HOME" => VAGRANT_HOME
  }
  # start the services
  config.vm.provision "shell", path: "./scripts/enable_services.sh", env: {
    "APP_NAME" => APP_NAME,
    "VAGRANT_HOME" => VAGRANT_HOME
  }
  
end
