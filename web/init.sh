sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo pip3 install --upgrade django
#sudo pip3 install --upgrade gunicorn
#sudo nano /usr/sbin/gunicorn-debian
#sudo nano /usr/bin/gunicorn
#sudo nano /usr/bin/gunicorn_django
#sudo nano /usr/bin/gunicorn_paster

sudo ln -sf /home/box/web/etc/guniconf_hello.py   /etc/gunicorn.d/guniconf_hello
sudo ln -sf /home/box/web/etc/guniconf_django.py   /etc/gunicorn.d/guniconf_django
sudo /etc/init.d/gunicorn restart

sudo gunicorn -c /etc/gunicorn.d/guniconf_hello hello:app
#cd ask/
sudo gunicorn -c /etc/gunicorn.d/guniconf_django ask.wsgi:application
