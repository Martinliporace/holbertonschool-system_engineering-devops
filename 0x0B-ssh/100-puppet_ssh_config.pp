file_line { 'ssh_conf':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '      IdentityFile ~/.ssh/school',
  replace => true
}

file_line { 'quit_pass':
  path    => '/etc/ssh/ssh_config',
  line    => '     PasswordAuthentication no',
  replace => true
}
