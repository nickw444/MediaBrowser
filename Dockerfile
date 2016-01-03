FROM python:latest

WORKDIR /build
ADD . /build

RUN pip install -r requirements.txt

EXPOSE 8080
CMD python mediabrowser.py meinheld
#
