FROM ubuntu
 
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN apt-get -y install python3-pip
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
ADD ./grypar.com.conf /etc/apache2/sites-available/grypar.com.conf
EXPOSE 80 3500
CMD ["apache2ctl","-D","FOREGROUND"]