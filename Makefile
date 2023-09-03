app:
	python app.py

lint:
	isort ./
	black ./
	flake8 ./
	mypy --ignore-missing-imports ./