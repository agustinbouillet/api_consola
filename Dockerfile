FROM python:3.10-bullseye

WORKDIR /usr/src/app

# Linux packages
RUN apt update
RUN apt-get install -y gcc python3-dev
RUN apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev
RUN apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN apt-get install -y python3 python-dev python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
RUN apt-get install -y python3-venv --assume-yes
RUN apt-get install -y python3-pip libapache2-mod-wsgi-py3 --assume-yes
RUN apt-get install -y git
RUN apt-get install -y locales-all

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir setuptools
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir mysql-connector-python
RUN pip install --no-cache-dir -r requirements.txt

COPY ./data /app/
