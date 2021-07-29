FROM node:12-alpine

# work directory
WORKDIR /usr/app

# Copy dependencies first for effective caching
COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]