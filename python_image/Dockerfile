FROM python:3.10-slim

WORKDIR /main

RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]