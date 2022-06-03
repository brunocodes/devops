FROM node:14-slim

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN npm install

COPY . .

USER node

EXPOSE 8088

CMD ["npm", "run", "start"]