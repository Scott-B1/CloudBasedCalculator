FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python3-pip python3

COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip3 install -r requirement.txt

COPY . /app

EXPOSE 80

ENTRYPOINT ["python3"]

CMD ["src/app.py"]
