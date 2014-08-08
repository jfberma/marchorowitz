#!/bin/bash

test ! -f run/supervisord.pid || ./bin/supervisorctl stop all
test ! -f run/supervisord.pid || sleep 5
test ! -f run/supervisord.pid || sudo kill `cat run/supervisord.pid`
