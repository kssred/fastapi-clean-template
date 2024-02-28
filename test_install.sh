#!/bin/bash
project_domain="domain.com"
project_path=`pwd`

sed -i "s~dbms_template_path~$project_path~g" systemd/gunicorn.service
#sed -i "s~dbms_template_domain~$project_domain~g" nginx/site.conf src/config/settings.py
