uwsgi --stop uwsgi.pid
sudo fuser -k 5200/tcp
echo > logs/uwsgi.log
