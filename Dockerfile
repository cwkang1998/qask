FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY justasklah justasklah

COPY . .

EXPOSE 5000

CMD [ "python3", "app.py"]
