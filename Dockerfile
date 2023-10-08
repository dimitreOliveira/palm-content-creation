FROM python:3.10

EXPOSE 8501

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ["app.py", "configs.yaml", "./"]

CMD ["streamlit", "run", "app.py", "--server.port", "8501"]