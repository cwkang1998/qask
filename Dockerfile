FROM python:3.7
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "index.py"]