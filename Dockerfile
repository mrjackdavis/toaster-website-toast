FROM python:3.4.3

RUN apt-get -y update

ENV PHANTOMJS_VERSION 1.9.7

RUN \
  apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \
  mkdir -p /srv/var && \
  wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
  rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \
  ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs

RUN pip install Pillow
RUN pip install selenium
RUN pip install nap
RUN pip install boto
RUN apt-get install -y python3-setuptools
RUN pip install Toast_Python_SDK==0.1.4

ADD ./src/* /app/

ENTRYPOINT ["python"]

CMD ["/app/main.py","-u http://www.trioxis.com"]

EXPOSE 5000