FROM biansepang/weebproject:buster

WORKDIR /home/weebproject

RUN chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/


CMD ["bash", "start.sh"]