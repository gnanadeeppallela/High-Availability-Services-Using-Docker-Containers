# High-Availability-Services-Using-Docker-Containers

Steps to Perform Live Migration using Nginx Webserver

Host 1:

Step 1: Create container:
docker run--name container_name-nginx –d –p 8080:80 container_image_name


Step 2: Open application on browser
Open browser and check if the application is running:
http://localhost:8080

Step 3: Checkpoint:
docker checkpoint create --checkpoint-dir=/tmp container_name checkpoint2


Step4: Transfer to host 2:
scp –r /local_host_path_images/ user_host2@host2_ipaddress:/destination/path


Host 2:

Step 1: Create container:
docker run--name container_name-nginx –d –p 8080:80 container_image_name

Step 2: restore the docker:
docker start –checkpoint-dir=/local_images_directory –checkpoint=images_folder container name



 

