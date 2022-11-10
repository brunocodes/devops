# Dockerize spring boot API
Dockerized Spring Boot Application. The image will use you compiled jar file to run the application

# Run with Docker Compose
```
docker-compose up
```
use ```docker-compose down``` to breakdown the running container.
# Build Docker Image 
```
docker build -t spring-boot-docker.jar .
```

# Check Docker Image 
```
docker image ls
```

# Run Docker Image 
```
docker run -p 8080:8080 spring-boot-docker.jar
```