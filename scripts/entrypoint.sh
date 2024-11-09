#!/bin/bash

# Log message
echo "Running entrypoint script..."

# Migrate the database
#   IF I HAD ONE! - Mr. Turner
# python manage.py migrate

echo "Entrypoint script complete."

# Execute the main container command
exec "$@"
