# Using Puppet to create a custom HTTP header

exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# install nginx on a server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# custom header response(X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# start webserver service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
