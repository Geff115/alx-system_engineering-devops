# This puppet manifest changes the OS configuration.

user { 'holberton':
  ensure     => 'present',
  managehome => true,
  home       => '/home/holberton',
  shell      => '/bin/bash',
}

file { '/home/holberton':
  ensure  => 'directory',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0700',
  recurse => true,
}

exec { 'unlock-holberton-user':
  command => '/usr/sbin/usermod -U holberton',
  onlyif  => '/bin/grep -q "^holberton:" /etc/shadow && /bin/grep -q "^holberton:!!" /etc/shadow',
}
