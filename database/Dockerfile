# Use official PostgreSQL image
FROM postgres:15-alpine

# Set environment variables for initialization
ENV POSTGRES_DB=productdb
ENV POSTGRES_USER=productuser
ENV POSTGRES_PASSWORD=productpass

# Create directory for initialization scripts
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy initialization script
COPY database/init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD pg_isready -U productuser -d productdb || exit 1

# PostgreSQL automatically runs init scripts on first startup
# No need to override CMD
