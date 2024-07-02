# This puppet file kills a process using exec
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => [ '/usr/bin', '/usr/sbin' ],
  returns => [0, 1],
}
