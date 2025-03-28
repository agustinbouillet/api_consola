FROM python:3.10-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt ./

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    default-mysql-client \
    default-libmysqlclient-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python utilizando pip con --no-cache-dir 
# para reducir el tamaño de la imagen.
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY ./data /app/
