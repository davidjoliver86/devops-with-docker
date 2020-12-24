FROM ubuntu:20.04
COPY curler.sh /bin
RUN apt update && apt install -y curl
CMD [ "/bin/bash", "/bin/curler.sh" ]
