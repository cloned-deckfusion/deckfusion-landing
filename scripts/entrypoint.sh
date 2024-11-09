#!/bin/bash

# Log message
echo "Running entrypoint script..."

# Migrate the database
# python manage.py migrate

echo "Entrypoint script complete."

# Execute the main container command
exec "$@"
