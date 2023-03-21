FROM node:16

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./

RUN npm install yarn 

RUN yarn add global create-react-app

RUN yarn

COPY . /app

CMD ["yarn", "start"]