package:
	rm -rf dist/ build/
	python3 setup.py sdist
	twine upload dist/*

clean:
	rm -rf build dist docs/build kedro/html pip-wheel-metadata .mypy_cache .pytest_cache
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +

format:
	isort --recursive inflate
	black -l 88 inflate

lint:
	pylint -j0 inflate --disable=bad-continuation

test:
	pytest -v