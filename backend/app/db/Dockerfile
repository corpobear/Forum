# Use an official PostgreSQL image as a parent image
FROM postgres:latest

# Environment variables for PostgreSQL
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

# Copy the SQL script to initialize the database
COPY create.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port
EXPOSE 5432