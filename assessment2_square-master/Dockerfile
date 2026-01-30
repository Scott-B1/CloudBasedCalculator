FROM golang:latest

WORKDIR /src/
COPY src/ /src/
EXPOSE 80

RUN go build -o main.go .
CMD ["/src/main.go"]
