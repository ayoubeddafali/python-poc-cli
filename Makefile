.PHONY: default

default: dev

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest

dev:
	PYTHONPATH=./src python setup.py bdist_wheel && pip install dist/ck8s-0.0.2-py2.py3-none-any.whl --force-reinstall

