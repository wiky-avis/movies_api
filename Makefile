run:
	python manage.py api

install:
	pip install -r requirements.txt

install-linters:
	pip install isort black flake8

flake8-check:
	flake8 --config=.flake8

black-check:
	black . --config pyproject.toml --check

isort-check:
	isort -rc -c . --diff

black:
	black . --config pyproject.toml

isort:
	isort -rc .

linters-check: isort-check black-check flake8-check

linters: isort black flake8-check
