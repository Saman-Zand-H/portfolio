FROM node:18-alpine

WORKDIR /usr/src/app/frontend

COPY package.json package-lock.json ./
RUN npm i -g vue && npm i

COPY . .

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
