#!/usr/bin/env bash
#Prepare your web servers
apt-get update -y
apt-get upgrade -y
apt-get install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx start
