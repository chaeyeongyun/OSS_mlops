FROM ubuntu:20.04


LABEL "MAINTAINER"="changjoy <ui88g216@gmail.com>"

RUN apt-get update && apt-get upgrade -y
RUN apt install curl -y
RUN apt install python3-pip -y
RUN pip3 install flask 
RUN pip3 install pillow 

EXPOSE 5000

ENTRYPOINT python app.py