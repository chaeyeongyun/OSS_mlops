FROM ubuntu:20.04

WORKDIR /Users/yunchaeyeong/Desktop/mlops/OSS_mlops
COPY  . .

LABEL "MAINTAINER"="changjoy <ui88g216@gmail.com>"

RUN apt-get update && apt-get upgrade -y
RUN apt install curl -y
RUN apt install python3-pip -y
RUN pip3 install flask 
RUN pip3 install pillow 

EXPOSE 5000
EXPOSE 80


ENTRYPOINT python3 app.py