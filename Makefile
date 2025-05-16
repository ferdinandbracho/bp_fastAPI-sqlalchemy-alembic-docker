init:
	python3 -m venv venv && . venv/bin/activate && pip install uv && uv pip install --no-cache-dir -r requirements.txt && pre-commit install && pre-commit run --all-files