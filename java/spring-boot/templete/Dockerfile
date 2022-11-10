FROM openjdk:8
WORKDIR /usr/src/app
COPY target/spring-boot-docker.jar ./spring-boot-docker.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/src/app/spring-boot-docker.jar"]