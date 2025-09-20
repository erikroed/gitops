FROM python:3.12-slim

WORKDIR /usr/src/app

COPY main.py requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME=World

CMD ["python", "main.py"]
