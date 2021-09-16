FROM python:3.7-slim

WORKDIR /app

COPY main.py /app
COPY nlp.py /app
COPY save_csv.py /app
COPY requirements.txt /app
COPY mongo.py /app
COPY utters/uttersEN.json /app
COPY utters/uttersFR.json /app
COPY app/ /app
COPY prediction.py /app
COPY function_wikiquote.py /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]