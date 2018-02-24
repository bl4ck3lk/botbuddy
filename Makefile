install:
	( \
	virtualenv -p python3.6 venv; \
	source venv/bin/activate; \
	pip install -Ur requirements.txt; \
	python setup.py install; \
	)

clean:
	rm -rf venv
	find . -name "*.pyc" -type f -delete
