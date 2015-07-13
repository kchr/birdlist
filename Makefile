WEBPY_ENV=test

dev:
	pip install -r requirements/dev.txt

prod:
	pip install -r requirements/dev.txt

tests:
	nosetests
