# This is a puppet manifest that will configure an ssh client
file { '/home/gabriel/.ssh/config':
  ensure  => file,
  mode    => '0600',
  owner   => 'gabriel',
  group   => 'gabriel',
  content => @("EOF")
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  EOF
}
