#Create file

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  path    => '/tmp/school',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0744'
}