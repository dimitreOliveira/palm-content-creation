app:
	streamlit run app.py

lint:
	isort ./
	black ./
	flake8 ./
	mypy --ignore-missing-imports ./