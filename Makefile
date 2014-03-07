.PHONY: test dist upload

test:
	pyvows sockmonkey/test

dist:
	python setup sdist

upload: dist
	python setup sdist upload
