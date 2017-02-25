Provisioning a new site
=======================

## Required packages

* nginx
* Python 3
* Git
* pip
* virtualenv

e.g. on Ubuntu:

```
sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv
```

## Nginx Virtual Host config

* See `nginx.template.conf`
* Replace SITENAME and USERNAME with e.g. `staging.mydomain.party` and `ajensen`

## Upstart Job

* See `gunicorn-upstart.template.conf`
* Replace SITENAME and USERNAME with e.g. `staging.mydomain.party` and `ajensen`

## Folder structure:

Assume we already have a user account at `/home/USERNAME`:

```
/home/USERNAME
 - sites
   - SITENAME
     - database
     - source
     - static
     - virtualenv
```