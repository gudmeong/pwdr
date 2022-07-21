FROM biansepang/weebproject:buster

RUN mkdir /home/weebproject \
WORKDIR /home/weebproject

RUN chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/


CMD ["bash", "start.sh"]