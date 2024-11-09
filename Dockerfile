# Set Python runtime
FROM python:3.11.5-slim-bookworm AS backend_base

# Set maintainer
LABEL maintainer="Sean O'Leary <seamicole@gmail.com>"

# Set build-time environment variables
ARG BACKEND_SECRET_KEY
ENV BACKEND_SECRET_KEY=${BACKEND_SECRET_KEY}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev

# Clean up APT when done
RUN rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Delete requirements.txt
RUN rm -f requirements.txt

# Copy the project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app

# Copy entrypoint scripts
COPY scripts/entrypoint.sh /usr/local/bin/

# Set entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Run command
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]
