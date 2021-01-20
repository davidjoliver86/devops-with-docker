FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8

WORKDIR /app

RUN apt update && \
    apt install -y curl python && \
    curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
    chmod a+x /usr/local/bin/youtube-dl && \
    apt-get purge -y --auto-remove curl && \ 
    rm -rf /var/lib/apt/lists/* && \
    useradd -m app && \
    /bin/chown -R app:app /app

USER app

ENTRYPOINT ["/usr/local/bin/youtube-dl"] 
