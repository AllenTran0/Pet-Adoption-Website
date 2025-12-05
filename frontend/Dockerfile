FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install 

RUN npm install @auth0/auth0-react

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]