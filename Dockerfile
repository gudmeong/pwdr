FROM gengkapak/app:latest

WORKDIR /home/cok/

RUN chmod 777 /home/cok/ \
    && mkdir /home/cok/bin/
COPY . .

CMD ["bash", "start.sh"]