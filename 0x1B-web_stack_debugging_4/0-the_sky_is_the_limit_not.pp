# This script increases the ULIMIT for the NGINX default file to 4096

exec { 'increase-file-limit-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'restart-nginx-service':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
