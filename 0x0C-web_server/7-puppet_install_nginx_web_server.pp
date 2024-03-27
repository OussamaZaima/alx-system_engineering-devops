# install and manage nginx server configuration using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
  provider => shell,
}

exec {'redirect_me':
  command => 'sudo sed -i "/listen 80 default_server;/a \\\trewrite ^/redirect_me https://github.com/Dtikoli permanent;" /etc/nginx/sites-available/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
