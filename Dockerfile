FROM python:3.11-slim
LABEL authors="levto"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir-r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]