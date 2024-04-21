# 1-install_a_package.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==3.0.3',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 3.0.3"',
}
