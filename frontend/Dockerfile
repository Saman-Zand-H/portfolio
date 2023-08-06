FROM node:14-alpine AS build

WORKDIR /usr/src/app/frontend

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY --from=build /usr/src/app/frontend/dist /usr/share/nginx/html

# Expose port 80 for Nginx (optional, only if needed to access from the host)
EXPOSE 80
