init:
	pip install --no-cache-dir --upgrade -r requirements.txt
	pre-commit install
	pre-commit run --all-files