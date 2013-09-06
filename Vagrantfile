require "yaml"

# Load up our vagrant config files -- vagrantconfig.yaml first
_config = YAML.load(File.open(File.join(File.dirname(__FILE__),
                    "vagrantconfig.yaml"), File::RDONLY).read)

# Local-specific/not-git-managed config -- vagrantconfig_local.yaml
begin
    _config.merge!(YAML.load(File.open(File.join(File.dirname(__FILE__),
                   "vagrantconfig_local.yaml"), File::RDONLY).read))
rescue Errno::ENOENT # No vagrantconfig_local.yaml found -- that's OK; just
                     # use the defaults.
end

CONF = _config
MOUNT_POINT = '/home/vagrant/project'

Vagrant.configure("2") do |config|
    config.vm.box = "lucid32"
    config.vm.box_url = "http://files.vagrantup.com/lucid32.box"

    config.vm.network :forwarded_port, guest: 8000, host: 8000
    config.vm.network :forwarded_port, guest: 3306, host: 3306

    #nfs needs to be explicitly enabled to run. 
    if CONF['nfs'] == false or RUBY_PLATFORM =~ /mswin(32|64)/
    config.vm.synced_folder ".", MOUNT_POINT
    else 
        config.vm.synced_folder ".", MOUNT_POINT, nfs: true
    end

    # Add to /etc/hosts: 33.33.33.24 dev.playdoh.org
    config.vm.network :private_network, ip: "33.33.33.24"

    config.vm.provision :puppet do |puppet|
        puppet.manifests_path = "puppet/manifests"
        puppet.manifest_file  = "vagrant.pp"
    end
end
