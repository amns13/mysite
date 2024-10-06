# Default is `bin/sh` which does not support all the commands, specifically, `source`
SHELL := /bin/bash

makemigrations: activate
	python mysite/manage.py makemigrations

migrate: activate
	python mysite/manage.py migrate

activate:
	source .venv/bin/activate

