#!/bin/bash  -x

yum update -y
yum install httpd -y
cd /var/www/html
