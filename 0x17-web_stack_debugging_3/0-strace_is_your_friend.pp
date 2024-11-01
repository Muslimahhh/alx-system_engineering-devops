# This code replaces the wrong filename with the right one
exec { 'replace-wordpress-phpp-with-php':
  environment => ['DIRECTORY=/var/www/html/wp-settings.php',
                  'OLD_VALUE=phpp',
                  'NEW_VALUE=php'],
  command     => 'sudo sed -i "s/$OLD_VALUE/$NEW_VALUE/" $DIRECTORY',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
