#config server

package { 'nginx':
provider => 'apt',
}
exec {'hlbtn_page':
command => '/usr/bin/sudo /bin/echo Holberton School > /var/www/html/index.nginx-debian.html',
}
exec {'redirect_page':

command => '/usr/bin/sudo /bin/sed -i "66i rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
}
exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
