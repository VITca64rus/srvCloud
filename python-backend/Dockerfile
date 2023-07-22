FROM python:3.9-alpine

RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /python-backend/app

RUN apk --update add
RUN apk add libc-dev libffi-dev git bind-tools bash \ 
        && apk add --virtual build-deps gcc python3-dev musl-dev \
        && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt

RUN apk del build-deps

COPY ./ /python-backend/

ENTRYPOINT [ "/python-backend/app/entrypoint.sh" ]
