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
