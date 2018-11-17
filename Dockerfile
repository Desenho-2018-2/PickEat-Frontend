FROM node:10-alpine

COPY package.json ./

RUN apk update \
  && apk add --update alpine-sdk python git \
  && npm install -g @angular/cli@7.0.4 \
  && apk del alpine-sdk python \
  && npm install --save @angular/material @angular/cdk \
  && yarn add @angular/material @angular/cdk @angular/animations \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache clean --force \
  && yarn cache clean \
  && sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd 

ENV NODE_ROOT pickeat-api
RUN mkdir -p $NODE_ROOT
WORKDIR $NODE_ROOT

RUN npm i

EXPOSE 4200 49153

CMD [ "ng", "serve" ]