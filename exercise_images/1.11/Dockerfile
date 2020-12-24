FROM ubuntu:20.04

# Install node
RUN apt update && apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt install -y nodejs

# Initialize app folder
RUN mkdir /app
WORKDIR /app

# Install app requirements
COPY package.json /app
COPY package-lock.json /app
RUN npm install

# Copy app to container and start server
COPY . /app
EXPOSE 8000
CMD ["npm", "start"]
