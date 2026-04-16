#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "======================================"
echo "TOEBEANS Backend Verification Test"
echo "======================================"
echo ""

# Check Python
echo -n "✓ Checking Python installation... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}OK${NC} ($PYTHON_VERSION)"
else
    echo -e "${RED}FAILED${NC} (Python 3 not found)"
    exit 1
fi

# Check Virtual Environment
echo -n "✓ Checking virtual environment... "
if [ -d "venv" ]; then
    echo -e "${GREEN}OK${NC} (venv directory exists)"
else
    echo -e "${YELLOW}NOT FOUND${NC} (creating venv...)"
    python3 -m venv venv
    echo -e "${GREEN}Created${NC}"
fi

# Activate virtualenv
source venv/bin/activate

# Check Django
echo -n "✓ Checking Django installation... "
if python -c "import django" 2>/dev/null; then
    DJANGO_VERSION=$(django-admin --version)
    echo -e "${GREEN}OK${NC} ($DJANGO_VERSION)"
else
    echo -e "${YELLOW}NOT FOUND${NC} (installing...)"
    pip install -q Django==4.2.7 Pillow==10.1.0 python-decouple==3.8
    echo -e "${GREEN}Installed${NC}"
fi

# Check database
echo -n "✓ Checking database... "
if [ -f "db.sqlite3" ]; then
    echo -e "${GREEN}OK${NC} (database exists)"
else
    echo -e "${YELLOW}NOT FOUND${NC} (running migrations...)"
    python manage.py migrate -q
    echo -e "${GREEN}Created${NC}"
fi

# Check project structure
echo ""
echo "✓ Checking project structure:"
files=(
    "manage.py"
    "toebeans/settings.py"
    "toebeans/urls.py"
    "store/models.py"
    "store/views.py"
    "store/urls.py"
    "store/admin.py"
    "store/forms.py"
    "store/templates/store/base.html"
    "store/static/store/css/base.css"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✓${NC} $file"
    else
        echo -e "  ${RED}✗${NC} $file"
    fi
done

echo ""
echo "✓ Checking Django apps configuration..."
python manage.py check --deploy -q
if [ $? -eq 0 ]; then
    echo -e "  ${GREEN}✓${NC} All systems operational"
else
    if python manage.py check -q 2>/dev/null; then
        echo -e "  ${YELLOW}✓${NC} Development mode ready (DEBUG enabled)"
    else
        echo -e "  ${RED}✗${NC} Configuration error detected"
    fi
fi

echo ""
echo "======================================"
echo "Verification Complete!"
echo "======================================"
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  Website: http://localhost:8000"
echo "  Admin Panel: http://localhost:8000/admin/"
echo ""
