sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test_wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test_django
#sudo /etc/init.d/gunicorn restart
#gunicorn -c /etc/gunicorn.d/test_django ask.wsgi:application
cd /home/box/web/ask/
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
cd /home/box/web
sudo gunicorn -b 0.0.0.0:8080 hello:app &