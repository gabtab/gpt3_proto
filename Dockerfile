FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN apt-get -y install python3-pip
RUN apt-get -y install tzdata

RUN pip3 install --upgrade pip
RUN apt-get -y install mysql-server
RUN apt-get -y install libmysqlclient-dev

COPY requirements.txt /var/www/grypar.com/requirements.txt
RUN pip install -r /var/www/grypar.com/requirements.txt

ADD . /var/www/grypar.com
RUN which python3
RUN . /var/www/grypar.com/my_env/bin/activate
RUN which python3


#ADD ./grypar.com.conf /etc/apache2/sites-available/grypar.com.conf
RUN a2dissite 000-default.conf
RUN a2ensite grypar.com
RUN a2enmod rewrite
RUN a2enmod ssl
#RUN service apache2 reload

#RUN service apache2 restart

EXPOSE 80 443
CMD ["apache2ctl","-D","FOREGROUND"]
