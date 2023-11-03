FROM mariadb:11.1.2-jammy

COPY ./init.sql /docker-entrypoint-initdb.d