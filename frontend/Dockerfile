FROM node:18-alpine AS build

WORKDIR /usr/src/app/frontend

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY --from=build /usr/src/app/frontend/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf 

EXPOSE 80
EXPOSE 8080

ENTRYPOINT [ "sh", "entrypoint.sh" ]
