FROM gengkapak/noc

WORKDIR /home/gengkapak/dclxvi/

RUN chmod 777 /home/gengkapak/dclxvi/ \
    && mkdir /home/gengkapak/dclxvi/bin/
COPY . .

CMD ["bash", "start.sh"]