# A puppet manifest that fixes a a file extension in on a web server

$error_file = '/var/www/html/wp-settings.php'

#fixing lines containing "phpp" with "php"

exec { 'fix_extension':
  command => "sed -i 's/phpp/php/g' ${error_file}",
  path    => ['/bin','/usr/bin']
}
