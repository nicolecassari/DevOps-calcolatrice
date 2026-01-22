FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd -m appuser  #uso RUN come se avessi creato una VM 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt   #per ottimizzare lo strato docker

COPY . .
RUN chown -R appuser:appuser /app
USER appuser

CMD ["python", "calcolatrice.py"]