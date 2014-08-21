#!/bin/bash

echo "shutting down servers"
bin/supervisorctl stop all
echo "getting latest code"
git pull
echo "running update scripts"
#git describe > gitDescribe.txt
. bin/activate && make
bin/buildout
bin/django syncdb --noinput
bin/django migrate --noinput
#bin/django check_permissions
bin/django collectstatic -c -l --noinput
echo "starting servers"
bin/supervisorctl start all