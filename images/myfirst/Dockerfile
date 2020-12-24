FROM ubuntu:20.04

WORKDIR /mydir
RUN apt update && apt install -y wget

RUN touch hello.txt
COPY local.txt .
RUN wget http://example.com/index.html
