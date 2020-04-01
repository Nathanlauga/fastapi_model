FROM python:3.7-slim

RUN mkdir /data
RUN mkdir /api

ADD requirements.txt /api/
WORKDIR /api

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000:8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]