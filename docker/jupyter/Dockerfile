FROM python:3.7-slim

RUN mkdir /nb

ADD requirements.txt /nb/
WORKDIR /nb

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8888:8888

ENTRYPOINT ["/bin/bash", "-c", "jupyter notebook --ip=0.0.0.0 --allow-root --path=/nb/"]
