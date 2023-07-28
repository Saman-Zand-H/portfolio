FROM node:20-alpine3.17

WORKDIR /usr/src/app/frontend

COPY package.json package.json

RUN npm i -g @vue/cli
RUN npm i -g serve
RUN npm install

COPY . .

ENV HOST=0.0.0.0

CMD ["npm", "run", "serve"]
