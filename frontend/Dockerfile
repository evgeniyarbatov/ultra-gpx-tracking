FROM --platform=linux/amd64 node:12.18.1
 
WORKDIR /app
COPY . /app

RUN npm install --production

EXPOSE 8080

CMD ["npm","start"]