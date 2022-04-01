
# IP Reputation Service
## Introduction
Provides an IP address Reputation service. 

This will return the following information about an IP address

- IP Address Owner _string_
- IP Address Reverse Lookup _string_
- Is it a TOR exit Node? 
- Is the IP address in the SpamHaus DB?
- Is IP address in BOT databases?


## Technology
There are three versions of the API.
- Python3 Fast API
- GoLang
- Type Script

## Local Development
Local development is done using Docker-compose

### Python

- change to the py directory
- run docker-compose up

Test the endpoint from a browser or with Postman
```
http://localhost:8000/v1/health
```

### Go Lang

### TypeScript Node