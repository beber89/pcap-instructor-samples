FROM python:latest
RUN pip install flask
RUN pip install -U flask-cors
ENTRYPOINT  "/bin/bash"