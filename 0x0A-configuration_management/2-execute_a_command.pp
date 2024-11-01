# Kill a running process using Puppet manifests

exec { 'killProcess':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
