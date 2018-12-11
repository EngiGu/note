FROM ubuntu:16.04

MAINTAINER sayheya "sayheya@163.com"

WORKDIR /code
ENV CODE_PATH=/code

RUN rm /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list
COPY require.txt ${CODE_PATH}

RUN apt-get update && \
    apt-get install -y curl wget gcc software-properties-common vim tzdata && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    apt-get update && \
    apt-get install -y python3.6 python3.6-dev python3.6-venv && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.6 get-pip.py && rm get-pip.py && \
    cd ${CODE_PATH} && pip3.6 install -r require.txt -i https://mirrors.aliyun.com/pypi/simple/ && \
    echo "Asia/Shanghai" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm /tmp/* -rf  

# 启动cron
CMD ["/usr/sbin/cron"]
CMD ["/bin/bash"]

