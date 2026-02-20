#!/usr/bin/env sh
set -e

echo "Running migrations..."
cd src/
uv run alembic upgrade head
echo "Migrations applied."

echo "Starting bot..."
cd ../
exec "$@"