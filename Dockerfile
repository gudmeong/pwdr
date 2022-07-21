FROM biansepang/weebproject:buster

WORKDIR /home/weebproject

RUN chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/
COPY . .

CMD ["bash", "start.sh"]