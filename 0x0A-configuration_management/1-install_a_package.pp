# Using Puppet, install flask from pip3.

package { 'installFlask':
      ensure   => '2.1.0',
      provider => 'pip3',
      name     => 'flask',
}

package { 'installWerkzeug':
      ensure   => '2.1.1',
      provider => 'pip3',
      name     => 'Werkzeug',
}
