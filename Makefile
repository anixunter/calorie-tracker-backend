format:
	black .

check-format:
	black --check .

lint: check-format
	flake8 .