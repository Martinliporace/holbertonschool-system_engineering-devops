#exec comm

exec { 'death to mfckr':
  command => '/usr/bin/pkill -f killmenow',
}
