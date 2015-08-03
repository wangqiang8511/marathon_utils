FROM ubuntu:14.04

MAINTAINER Wang Qiang "wangqiang8511@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    wget python python-setuptools python-pkg-resources \
    python-pip

RUN pip install virtualenv

RUN mkdir -p /opt/marathon_utils
ADD . /opt/marathon_utils

WORKDIR /opt/marathon_utils
RUN make clean && make install

ENTRYPOINT ["/opt/marathon_utils/bin/python", "-m", "marathon_utils.marathon"]
