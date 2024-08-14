# This Puppet manifest fixes the HTTP 500 status code indicating an error in the Apache server

apache::mod::rewrite { 'enabled':
  ensure => 'present',
}

service { 'apache2':
  ensure => 'restarted',
}

file { '/var/www/html/index.php':
  ensure  => 'file',
  owner   => 'apache',
  group   => 'apache',
  mode    => '0644',
  content => template('index.php.erb'),
}
