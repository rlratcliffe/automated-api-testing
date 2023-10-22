# Service Virtualization

To start the server:
```
docker build -t mountebank-server-with-templates .
docker run --name mountebank-animal-server -p 2525:2525 -p 8090:8090 -p 8091:8091 -it mountebank-server-with-templates
```

To clean up the server:
`docker rm mountebank-animal-server`
