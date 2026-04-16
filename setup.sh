#!/bin/bash

# TOEBEANS Django Backend Setup Script

echo "======================================"
echo "TOEBEANS Backend Setup"
echo "======================================"
echo ""

# Create virtual environment
echo "1. Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "2. Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create database
echo "3. Running migrations..."
python manage.py migrate

# Create superuser
echo "4. Creating superuser account..."
echo "Please enter superuser details:"
python manage.py createsuperuser

# Load sample data
echo "5. Creating sample data..."
python manage.py shell << EOF
from store.models import Brand, Category

# Create categories
categories = [
    {'name': 'Men'},
    {'name': 'Women'},
]

for cat in categories:
    Category.objects.get_or_create(name=cat['name'])

# Create brands
brands = [
    {'name': 'Nike', 'description': 'Premium athletic footwear'},
    {'name': 'Adidas', 'description': 'Quality sports shoes'},
    {'name': 'Puma', 'description': 'Performance and style'},
    {'name': 'Prada', 'description': 'Luxury Italian footwear'},
    {'name': 'Dior', 'description': 'Elegant designer shoes'},
    {'name': 'Louboutin', 'description': 'Iconic luxury heels'},
    {'name': 'Jimmy Choo', 'description': 'Designer footwear'},
    {'name': 'Skechers', 'description': 'Comfortable casual shoes'},
]

for brand in brands:
    Brand.objects.get_or_create(name=brand['name'], defaults={'description': brand['description']})

print("Sample data created successfully!")
EOF

# Collect static files
echo "6. Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Admin portal: http://localhost:8000/admin"
echo ""
