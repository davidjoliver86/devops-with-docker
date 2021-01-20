FROM ubuntu:20.04

RUN apt-get update && apt-get install -y docker.io && rm -rf /var/lib/apt/lists

WORKDIR /app

COPY dockerizer.py /app

ENTRYPOINT [ "python3", "dockerizer.py" ]
