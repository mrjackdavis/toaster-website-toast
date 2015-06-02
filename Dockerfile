FROM python:3.4.3

RUN apt-get -y update

RUN pip install Pillow
RUN pip install selenium
RUN pip install nap
RUN pip install boto

# ADD ./utils/* /utils/

# RUN /utils/install_phantomjs.sh

# RUN apt-get update && apt-get install -y g++ flex bison gperf ruby perl libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev libpng-dev libjpeg-dev make git libqt5webkit5-dev 

# RUN git clone git://github.com/ariya/phantomjs.git && cd phantomjs && git checkout 2.0 && ./build.sh --confirm

ENV PHANTOMJS_VERSION 1.9.7

RUN \
  apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \
  mkdir -p /srv/var && \
  wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
  rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \
  ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs

ADD ./src/* /app/

ENTRYPOINT ["python"]

CMD ["/app/main.py","-u http://www.google.com"]

EXPOSE 5000