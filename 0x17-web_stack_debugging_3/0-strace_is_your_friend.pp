# find out why Apache returns a 500 error, fix, and automate using puppet

exec { 'fix-wordpress':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
