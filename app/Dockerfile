FROM ubuntu:xenial

MAINTAINER Vladimir Ivashkin <illusionww@gmail.com>

RUN apt-get update && apt-get install -y \
        python3 python3-dev python3-pip

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "app:app"]
