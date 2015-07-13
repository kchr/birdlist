WEBPY_ENV = test

dev:
	pip install -r requirements/dev.txt

prod:
	pip install -r requirements/prod.txt

serve:
	python ./main.py $(WEBPY_LISTEN)

tests:
	WEBPY_ENV=$(WEBPY_ENV) nosetests
