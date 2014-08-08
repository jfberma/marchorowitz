Django Nginx Jumpstart
======================

This repo contains a template for quickly setting up a Django/Nginx/Postgres/Supervisor environment. Inspired by https://github.com/oleksandr/django-buildout-layout.

Get Started
===========

1. Duplicate this repo: 
```
git clone --bare git@github.com:jfberma/django-nginx-jumpstart.git
cd django-nginx-jumpstart
git push --mirror [YOUR_NEW_REPO_URL]
```
2. ```cd``` into the new repo and edit ```buildout.cfg``` to include your enviroment's database details
