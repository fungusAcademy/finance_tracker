# Build script for Render.com

echo "=== Starting Build Process ==="

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Create superuser
echo "Creating superuser..."
python manage.py create_superuser

echo "=== Build Completed Successfully ==="