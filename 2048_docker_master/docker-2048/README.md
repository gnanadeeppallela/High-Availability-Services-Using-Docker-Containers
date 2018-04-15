# docker-2048

a smaller docker version of 2048

Base on gabrielecirulli/2048(https://github.com/gabrielecirulli/2048)

Base on alpine

Base on nginx

#dockerfile

    FROM alpine:latest

    RUN apk --update add nginx

    COPY 2048 /usr/share/nginx/html

    EXPOSE 80

    CMD ["nginx", "-g", "daemon off;"]

# run the docker container with your own build

    docker build -t "docker-2048" .
    docker run -d -p 8080:80 docker-2048

	# Access the game

    http://127.0.0.1:8080