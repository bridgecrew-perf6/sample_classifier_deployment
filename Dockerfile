FROM postgres

ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB postgres

COPY predictions.sql /docker-entrypoint-initdb.d/

#RUN service postgresql start

WORKDIR /app
COPY requirements.txt ./

RUN apt-get update

RUN apt-get install -y python3.10 libpq-dev
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080