package:
	rm -rf dist/ build/
	python3 setup.py sdist
	twine upload dist/*

format:
	isort --recursive inflate
	black -l 88 inflate

lint:
	pylint -j0 inflate --disable=bad-continuation