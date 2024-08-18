# This Puppet manifest fixes the HTTP 500 status code indicating an error in the Apache server

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

service { 'apache2':
  ensure => 'restarted',
}
