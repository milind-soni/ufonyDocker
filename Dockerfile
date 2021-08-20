from alpine:latest

RUN apk add --no-cache py-pip python3-dev \
    && pip3 install --upgrade pip	 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
