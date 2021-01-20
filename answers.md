Dockerfiles are found in the `exercise_images` folder that matches the exercise number.
## 1-1
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
4672fa6ed44a        nginx               "/docker-entrypoint.…"   49 seconds ago      Exited (0) 33 seconds ago                       fervent_mayer
c15551a7aa17        nginx               "/docker-entrypoint.…"   50 seconds ago      Exited (0) 33 seconds ago                       quirky_matsumoto
a49252748084        nginx               "/docker-entrypoint.…"   51 seconds ago      Up 50 seconds               80/tcp              wizardly_euclid
```

## 1-2
```
docker ps -a:
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

docker images:
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

## 1-3
```
docker run -it devopsdockeruh/pull_exercise
```
The password was: basics

The secret message is: "This is the secret message"

## 1-4
Run container:
```
docker run -it -d --name derp devopsdockeruh/exec_bash_exercise
```
Enter container:
```
docker exec -it derp bash
```
Inside container:
```
tail -f ./logs.txt
```
Secret message is: "Docker is easy"

## 1-5
Creating a new container:
```
docker run -it ubuntu:latest
```
Launched a shell - in the shell:
```
apt update && apt install -y curl
exit
```
Start the container back up:
```
docker start ecstatic_bhaskara
```
Run the command:
```
docker exec -it ecstatic_bhaskara sh -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website;'
```
Output:
```
Input website:
helsinki.fi
Searching..
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://www.helsinki.fi/">here</a>.</p>
</body></html>
```

## 1-6
```
docker run --rm -it docker-clock
```

## 1-7
```
docker run --rm -it curler
```

## 1-8
```
touch logs.txt
docker run --rm -it -v $(pwd)/logs.txt:/usr/app/logs.txt devopsdockeruh/first_volume_exercise
```
Secret message is "Volume bind mount is easy"

## 1-9
```
docker run -d -p 8080:80 devopsdockeruh/ports_exercise
```
In a shell:
```
$ curl localhost:8080
Ports configured correctly!!
```

## 1-10
See 1-10/Dockerfile

## 1-11
See 1-11/Dockerfile
```
docker run --rm -it -p 8000:8000 -v $(pwd)/logs.txt:/app/logs.txt backend-example
```

## 1-12
I did not need to edit the Dockerfiles, I simply ran them with the `-e` parameter.

Frontend:
```
docker run --rm -d -p 5000:5000 -e API_URL=http://localhost:8000 frontend-example
```
Backend:
```
docker run --rm -d -p 8000:8000 -v $(pwd)/logs.txt:/app/logs.txt -e FRONT_URL=http://localhost:5000 backend-example
```

## 1-13
See 1-13/Dockerfile

## 1-14
See 1-14/Dockerfile

## 1-15
https://hub.docker.com/repository/docker/davidjoliver86/node-chuck

# Part 2

## 2-1
See 2-1/docker-compose.yml

## 2-2
See 2-2/docker-compose.yml

## 2-3
See 2-3/docker-compose.yml

## 2-4
As long as `compute` was scaled to at least two instances, I was able to successfully complete this.
```
docker-compose up -d --scale compute=2
```

## 2-5
See 2-5/docker-compose.yml

## 2-6
See 2-6/docker-compose.yml

## 2-7
See 2-7/docker-compose.yml

## 2-8, 2-9, 2-10
See 2-8/docker-compose.yml

# Part 3

## 3-1
### Frontend: before
```
$ docker image history frontend
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
61b487b668a1        4 weeks ago         /bin/sh -c #(nop)  CMD ["npm" "start"]          0B                  
76cff046f9bf        4 weeks ago         /bin/sh -c #(nop) COPY dir:9c7db2c149fe6cec6…   922kB               
d33ab77550cd        4 weeks ago         /bin/sh -c npm install                          212MB               
73ba75286ad7        4 weeks ago         /bin/sh -c #(nop) COPY file:8c39261088fecef3…   526kB               
fc0ff8b88d41        4 weeks ago         /bin/sh -c #(nop) COPY file:481f5a917e0a660a…   1.7kB               
9519f45703bf        4 weeks ago         /bin/sh -c #(nop) WORKDIR /app                  0B                  
23d57525f712        4 weeks ago         /bin/sh -c mkdir /app                           0B                  
6462ff9112cf        4 weeks ago         /bin/sh -c apt install -y nodejs                64.6MB              
fb06bf31aceb        4 weeks ago         /bin/sh -c curl -sL https://deb.nodesource.c…   40.7MB              
65c16404f1e1        4 weeks ago         /bin/sh -c apt update && apt install -y curl    42.5MB              
f643c72bc252        6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           6 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           6 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
<missing>           6 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B                
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:4f15c4475fbafb3fe…   72.9MB
```

### Frontend: after
```
$ docker image history frontend
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
2379d379e53c        5 minutes ago       /bin/sh -c #(nop)  CMD ["npm" "start"]          0B                  
95f25566bdd6        5 minutes ago       /bin/sh -c #(nop)  EXPOSE 5000                  0B                  
b146393b9e4f        5 minutes ago       /bin/sh -c #(nop) COPY dir:e666f314a660627b3…   921kB               
6a8fc0e229d2        5 minutes ago       /bin/sh -c apt update && apt install -y curl…   325MB               
707740425f25        8 minutes ago       /bin/sh -c #(nop) WORKDIR /app                  0B                  
d36bf2dfd540        8 minutes ago       /bin/sh -c #(nop) COPY multi:e4e32dc05746f4e…   528kB               
f643c72bc252        6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           6 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           6 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
<missing>           6 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B                
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:4f15c4475fbafb3fe…   72.9MB
```

### Backend: before
```
$ docker image history backend
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
e4b902e500f5        4 weeks ago         /bin/sh -c #(nop)  CMD ["npm" "start"]          0B                  
0282f755bc62        4 weeks ago         /bin/sh -c #(nop)  EXPOSE 8000                  0B                  
83ea1b8d1bf8        4 weeks ago         /bin/sh -c #(nop) COPY dir:937f199256f464a6e…   232kB               
44c15b022f0e        4 weeks ago         /bin/sh -c npm install                          18.1MB              
5b0f9c63081b        4 weeks ago         /bin/sh -c #(nop) COPY file:30878d3d68a2b46c…   64.1kB              
31b1a1ab4c9f        4 weeks ago         /bin/sh -c #(nop) COPY file:d617975225e72adc…   706B                
9519f45703bf        4 weeks ago         /bin/sh -c #(nop) WORKDIR /app                  0B                  
23d57525f712        4 weeks ago         /bin/sh -c mkdir /app                           0B                  
6462ff9112cf        4 weeks ago         /bin/sh -c apt install -y nodejs                64.6MB              
fb06bf31aceb        4 weeks ago         /bin/sh -c curl -sL https://deb.nodesource.c…   40.7MB              
65c16404f1e1        4 weeks ago         /bin/sh -c apt update && apt install -y curl    42.5MB              
f643c72bc252        6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           6 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           6 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
<missing>           6 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B                
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:4f15c4475fbafb3fe…   72.9MB
```

### Backend: after
```
$ docker image history backend
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
37560b317de3        18 minutes ago      /bin/sh -c #(nop)  CMD ["npm" "start"]          0B                  
eab8f80379b4        18 minutes ago      /bin/sh -c #(nop)  EXPOSE 8000                  0B                  
23df6406c793        18 minutes ago      /bin/sh -c #(nop) COPY dir:6319a688152b54e20…   232kB               
5671295a3bfc        18 minutes ago      /bin/sh -c apt update && apt install -y curl…   131MB               
efd3adbd1b07        33 minutes ago      /bin/sh -c #(nop) WORKDIR /app                  0B                  
da5d166caef9        33 minutes ago      /bin/sh -c #(nop) COPY multi:9ed5ff5268bec64…   64.9kB              
f643c72bc252        6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           6 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           6 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
<missing>           6 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B                
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:4f15c4475fbafb3fe…   72.9MB
```
Frontend image went from 434MB -> 399MB. Backend went from 239MB -> 204MB. Images still work when
used in the 2.8 stack.

## 3-2
https://github.com/davidjoliver86/node-chuck-norris

I used the Heroku orb to install the CLI, but I found that the orb's predefined jobs
and steps were rather buggy. There were other things that weren't obvious at first,
such as needing to explicitly call `checkout` and `setup_remote_docker`.

To get the server to respond to the random ephemeral port assigned, I just made the
`httpServer` listen to the `PORT` environment variable.

## 3-3
See 3-3/.
Included a `docker-compose.yml` for a more abstract way of running the containerized version.

## 3-4
See 3-4/.
Confirmed rootless images work with the 2-8 stack.

## 3-5
Before:
```
$ docker images | grep end
frontend                        nonroot             efc3756a45ba        20 minutes ago      400MB
backend                         nonroot             b48833686768        24 minutes ago      205MB
```
After:
```
$ docker images | grep end | grep alpine
frontend                        alpine              535ec53b5479        9 minutes ago       296MB
backend                         alpine              70310b5c4124        5 minutes ago       101MB
```
