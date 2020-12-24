FROM openjdk:8
COPY . /app

workdir /app
RUN ./mvnw package
EXPOSE 8080
CMD ["java", "-jar", "/app/target/docker-example-1.1.3.jar"]
