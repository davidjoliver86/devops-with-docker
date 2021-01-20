FROM ubuntu:20.04

COPY package*.json /app/

WORKDIR /app

# Install node
RUN apt update && apt install -y curl && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash && \
    apt install -y nodejs && \
    npm install && \
    rm -rf /var/lib/apt/lists && \
    apt-get purge -y --auto-remove curl

# Copy app to container and start server

COPY . /app
EXPOSE 5000
CMD ["npm", "start"]
