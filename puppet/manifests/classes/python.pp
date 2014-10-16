# Install python and compiled modules for project
class python {
    case $operatingsystem {
        centos: {
            package {
                ["python27-devel", "python27-libs", "python27-distribute", "python27-mod_wsgi"]:
                    ensure => installed;
            }

            exec { "pip-install":
                command => "easy_install -U pip",
                creates => "pip",
                require => Package["python27-devel", "python27-distribute"]
            }

            exec { "pip-install-compiled":
                command => "pip install -r $PROJ_DIR/requirements/compiled.txt",
                require => Exec['pip-install']
            }
        }

        ubuntu: {
            package {
                ["python2.7-dev", "python2.7", "libapache2-mod-wsgi", "python-wsgi-intercept", "python-pip"]:
                    ensure => installed;
            }

            exec { "pip-install-compiled":
                command => "pip install -r $PROJ_DIR/requirements/compiled.txt",
                require => Package['python-pip']
            }
        }
    }
}
