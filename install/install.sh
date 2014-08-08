#!/bin/bash

export PROJECT_ROOT=`pwd`

echo "Installing Prerequisites"
test ! -f /usr/bin/yum || sudo yum -y install ant-apache-regexp curl-devel fontconfig freetype gcc gcc-c++ libfontconfig.so.1 libfreetype.so.6 libstdc++.so.6 libxml2-devel libxslt-devel libxml2-devel libxslt-devel libyaml-devel make mysql mysql-devel openssl-devel pcre-devel s3cmd zlib-devel GeoIP-devel
test ! -f /opt/local/bin/port || sudo port install libgeoip libyaml memcached mysql56-server mysql56 openssl pcre redis s3cmd wget zlib

mkdir src
test -d src/Python-2.7.6 || tar zxv -C ./src/ -f install/download-cache/Python-2.7.6.tgz
test -d parts/python || mkdir -p parts/python
cd src/Python-2.7.6
./configure --prefix=$PROJECT_ROOT/parts/python
echo "Building Python 2.7.6"
make
echo "Installing Python 2.7.6"
make install
cd ../..

./parts/python/bin/python2.7 install/virtualenv.py -p ./parts/python/bin/python2.7 --no-site-packages .