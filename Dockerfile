# Set Python runtime
FROM python:3.11.5-slim-bookworm AS landing_base

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

# Install dependencies and Node.js without npm for Tailwind CSS
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && corepack enable && corepack prepare npm@latest --activate \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy npm package files and install npm dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the project files
COPY . .

# Build Tailwind CSS
RUN npm run build:css

# Collect Django static files
RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app

# Copy entrypoint scripts and make it executable
COPY scripts/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Run command
CMD ["sh", "-c", "uvicorn config.asgi:application --host 0.0.0.0 --port ${PORT:-8000}"]
