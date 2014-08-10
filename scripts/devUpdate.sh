#!/bin/bash

echo "shutting down servers"
bin/supervisorctl stop all
echo "getting latest code"
git pull
echo "running update scripts"
#git describe > gitDescribe.txt
bin/django syncdb
bin/django migrate
#bin/django check_permissions
echo "starting servers"
bin/supervisorctl start all
