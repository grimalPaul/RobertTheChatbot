FROM python:3.7-slim

WORKDIR /app

#on copie les fichiers du répertoire courant dans le dossier du container qui sera /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "main.py"]