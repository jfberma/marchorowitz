#!/bin/bash

echo "shutting down servers"
sudo scripts/shutdownSupervisor.sh
echo "getting latest code"
git pull
echo "running update scripts"
git describe > gitDescribe.txt
bin/django syncdb --noinput
bin/django migrate --noinput
bin/django check_permissions
echo "starting servers"
sudo bin/supervisord
