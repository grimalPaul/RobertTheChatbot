FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "main.py"]