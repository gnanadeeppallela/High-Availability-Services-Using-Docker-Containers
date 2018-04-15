ROM ubuntu:latest
MAINTAINER Gnanadeep "pallela.gnanadeep@gmail.com"
RUN apt-get update
RUN apt-get install -y npm
RUN npm install -g http-server
RUN apt-get install -y python python-pip wget
RUN apt-get install -y criu
RUN mkdir criu
WORKDIR criu
ADD server.py .
RUN mkdir dump_dir
EXPOSE 8000
CMD ["python","server.py"]
