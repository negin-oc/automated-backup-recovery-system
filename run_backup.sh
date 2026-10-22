#!/bin/bash
cd ~/backup_system
/usr/local/bin/docker-compose run --rm backup-system python /app/auto_backup.py >> ~/backup_system/cron_log.log 2>&1
