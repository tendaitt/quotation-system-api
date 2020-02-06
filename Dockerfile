# base image

FROM python:3.8.0-alpine

# dependencies

RUN apk update && \
    apk add --no-cache --virtual build-deps \
    openssl-dev libffi-dev gcc python3-dev musl-dev \
    bash bash-doc bash-completion \
    curl grep git openssh make cmake \
    postgresql-dev netcat-openbsd

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory of the container
WORKDIR /usr/quotation/server

# install requirements
COPY requirements.txt /usr/quotation/server/requirements.txt
RUN pip install -r requirements.txt

# entry script
COPY app.sh /usr/quotation/server/app.sh

# modify permissions to run script
RUN chmod +x /usr/quotation/server/app.sh

# copy code base
COPY . /usr/quotation/server
