#!/bin/bash

echo "shutting down servers"
bin/supervisorctl stop all
echo "getting latest code"
git pull
echo "running update scripts"
#git describe > gitDescribe.txt
bin/activate
bin/buildout
bin/django syncdb
bin/django migrate
#bin/django check_permissions
bin/django_static collectstatic -c -l --noinput
echo "starting servers"
bin/supervisorctl start all