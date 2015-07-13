WEBPY_ENV=test
WEBPY_LISTEN=127.0.0.1:8080

dev:
	pip install -r requirements/dev.txt

prod:
	pip install -r requirements/dev.txt

serve:
	python ./main.py $(WEBPY_LISTEN)

tests:
	WEBPY_ENV=$(WEBPY_ENV) nosetests
