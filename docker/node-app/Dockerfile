FROM node:14-slim

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN npm install

COPY ./app ./

EXPOSE 8080

CMD ["node", "/usr/src/app/server/server.js"]