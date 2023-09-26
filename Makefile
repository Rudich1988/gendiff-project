install:
	poetry install

gen-diff:
	poetry run gendiff -h

#build:
#	poetry build

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

selfcheck:
	poetry check

check:
	selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build
