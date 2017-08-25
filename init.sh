sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#gunicorn -c /etc/gunicorn.d/test ask.wsgi:application
cd /home/box/web/ask
sudo gunicorn --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application &
