FROM node:10-alpine

RUN apk update \
  && apk add --update alpine-sdk python git \
  && npm install -g @angular/cli@7.0.4 \
  && apk del alpine-sdk python \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache clean --force \
  && yarn cache clean \
  && sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd 

ENV NODE_ROOT /usr/app/
RUN mkdir -p $NODE_ROOT
WORKDIR $NODE_ROOT
COPY . .

RUN rm -rf node_modules/ && npm i

EXPOSE 4200