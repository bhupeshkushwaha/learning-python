FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src/ /app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers", "3"]

