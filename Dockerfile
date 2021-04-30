# syntax=docker/dockerfile:1
FROM python:3.8.9
RUN 'pip install pytest'
RUN 'pytest'

