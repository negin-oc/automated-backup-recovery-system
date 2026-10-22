FROM python:3.12-slim

WORKDIR /app

COPY app/ /app/app/

ENV PYTHONPATH=/app/app
ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/app/main.py"]
