#!/usr/bin/env sh

celery -A app beat -l INFO &
celery -A app worker -l INFO -n worker.whatever --concurrency=12 -Q default
