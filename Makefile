install:
	poetry install

gen-diff:
	poetry run gendiff -h

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	poetry run flake8 gendiff

check: test lint

build: check
		poetry build

.PHONY: install test lint check build
