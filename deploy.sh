#! /bin/bash

ssh -q devzabbix1.ufes.br 'cp -r zabbix-pg zabbix-pg-$(date +%s)'
rsync -avP ./ devzabbix1.ufes.br:zabbix-pg/