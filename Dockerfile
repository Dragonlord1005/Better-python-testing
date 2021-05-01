# syntax=docker/dockerfile:1
FROM python:3.8.9
COPY . /python-text-based-game-framework
WORKDIR /python-text-based-game-framework
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest"]
CMD tail -f /dev/null
