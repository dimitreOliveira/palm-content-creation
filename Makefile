FEATURE_NAME := palm_creator
TAG ?= latest

app:
	docker run --rm -p 8501:8501 ${FEATURE_NAME}:${TAG}

build:
	docker build -t ${FEATURE_NAME}:${TAG} .

lint:
	isort ./
	black ./
	flake8 ./
	mypy --ignore-missing-imports ./