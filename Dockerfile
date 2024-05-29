FROM python:3-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache postgresql-libs && \
apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers gcc musl-dev postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /backend
COPY ./backend /backend
WORKDIR /backend
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/

RUN adduser -D localapp
RUN chown -R localapp:localapp /vol
RUN chmod -R 755 /vol/web
USER localapp

CMD ["entrypoint.sh"]