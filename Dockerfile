FROM python:3.7.9-alpine3.13

WORKDIR /usr/src/app 

RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install datadog

COPY app.py /usr/src/app
COPY . /usr/src/app

EXPOSE 8083
CMD ["python3", "./app.py"]