FROM python:3.10-slim

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir  -r requirements.txt


COPY app  /project/app

WORKDIR /project/app

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

