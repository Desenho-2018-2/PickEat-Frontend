FROM alpine:3.8

RUN apk add --update \  
        python3-dev \
        py-pip \
        bash 

RUN pip install --upgrade pip

WORKDIR /home

## add requirements.txt file
ADD requirements.txt .

## install requirements
RUN pip3 install -r requirements.txt