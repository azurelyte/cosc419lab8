[code]#!/bin/bash
sudo yum install python-pip
sudo pip install --upgrade pip
sudo pip install flask
sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
sudo service httpd restart
sudo mkdir /var/www/lab8
sudo cp -r ./ /var/www/lab8
sudo cp ./myapp.conf /etc/httpd/conf.d/myapp.conf
sudo service httpd restart
