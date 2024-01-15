# syntax=docker/dockerfile:1

FROM python:3.9.18-bookworm

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]