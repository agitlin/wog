FROM python:3.8-alpine

WORKDIR /app
COPY reqs.txt .
COPY *.py .

COPY scores.txt .

RUN pip install --no-cache-dir -r reqs.txt

CMD ["python", "main_score.py"]