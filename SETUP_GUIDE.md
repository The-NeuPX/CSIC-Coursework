# TOEBEANS Backend Setup Guide

# Quick Start

## Prerequisites
- Python 3.8+
- pip
- Virtual environment

## Installation Steps

### 1. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account with email and password.

### 5. Load Initial Data
```bash
python manage.py shell << EOF
from store.models import Brand, Category

# Create categories
for cat in ['Men', 'Women']:
    Category.objects.get_or_create(name=cat)

# Create brands
brands = [
    ('Nike', 'Premium athletic footwear'),
    ('Adidas', 'Quality sports shoes'),
    ('Puma', 'Performance and style'),
    ('Prada', 'Luxury Italian footwear'),
    ('Dior', 'Elegant designer shoes'),
    ('Louboutin', 'Iconic luxury heels'),
    ('Jimmy Choo', 'Designer footwear'),
    ('Skechers', 'Comfortable casual shoes'),
]

for name, desc in brands:
    Brand.objects.get_or_create(name=name, defaults={'description': desc})

print("Setup complete!")
EOF
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Server will be available at: http://localhost:8000

## Access Points

### User Interface
- **Home Page**: http://localhost:8000/
- **Shop**: http://localhost:8000/shop/
- **Blog**: http://localhost:8000/blog/
- **About**: http://localhost:8000/about/
- **Research**: http://localhost:8000/research/
- **User Profile**: http://localhost:8000/profile/ (requires login)

### Authentication
- **Sign Up**: http://localhost:8000/signup/
- **Login**: http://localhost:8000/login/
- **Logout**: http://localhost:8000/logout/

### Admin Portal
- **Admin Dashboard**: http://localhost:8000/admin/
- Login with superuser credentials

## Admin Portal Features

### Managing Content

#### Products
1. Go to Admin → Store → Products
2. Click "Add Product" to create new products
3. Fill in:
   - Product name
   - Brand (select from list)
   - Category (Men/Women/etc)
   - Price
   - Description
   - Image (optional)
   - Stock quantity
   - Mark as featured (for homepage display)

#### Brands
1. Go to Admin → Store → Brands
2. Add/edit brands with name and description

#### Categories
1. Go to Admin → Store → Categories
2. Add/edit categories (Men, Women, etc.)

#### Blog Posts
1. Go to Admin → Store → Blog Posts
2. Create articles with:
   - Title
   - Content (full text)
   - Featured image
   - Author (automatically set to logged-in user)

#### User Management
1. Go to Admin → Authentication and Authorization → Users
2. View and manage user accounts
3. Access to user profiles with contact information

## Project Structure

```
toebeans_backend/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── setup.sh                  # Setup script
├── toebeans/                 # Main project folder
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
└── store/                    # Main app
    ├── migrations/          # Database migrations
    ├── templates/store/     # HTML templates
    │   ├── base.html        # Base template with navigation
    │   ├── index.html       # Homepage
    │   ├── shop.html        # Shop page
    │   ├── product_detail.html
    │   ├── brand_detail.html
    │   ├── category.html
    │   ├── blog.html        # Blog listing
    │   ├── blog_detail.html
    │   ├── login.html       # Login page
    │   ├── signup.html      # Registration page
    │   ├── profile.html     # User profile
    │   ├── aboutus.html     # About page
    │   └── research.html    # Research page
    ├── static/store/        # CSS and static files
    ├── admin.py             # Admin configuration
    ├── apps.py              # App configuration
    ├── forms.py             # Django forms
    ├── models.py            # Database models
    ├── urls.py              # App URL routing
    └── views.py             # View logic
```

## Database Models

### Brand
- name (unique)
- description
- created_at

### Category
- name (unique)
- description

### Product
- name
- brand (ForeignKey)
- category (ForeignKey)
- price
- description
- image
- stock
- is_featured
- created_at, updated_at

### UserProfile
- user (OneToOneField)
- phone
- address
- city, state, zipcode
- profile_picture
- created_at

### BlogPost
- title
- content
- author (ForeignKey to User)
- featured_image
- created_at, updated_at

## Authentication System

### User Registration
- Email-based signup
- Password validation
- Automatic UserProfile creation
- Email uniqueness validation

### User Login
- Email/password authentication
- Session management
- Automatic redirect to dashboard on login

### User Profile
- Editable user information
- Address and contact details
- Profile picture upload

## Features

✅ **User Authentication**
- Secure signup and login
- Password hashing
- Protected views (login required)

✅ **Product Management**
- Browseable product catalog
- Brand and category filtering
- Search functionality
- Product details page with related items

✅ **Blog System**
- Blog creation and viewing
- Featured images
- Author attribution
- Related posts

✅ **Admin Portal**
- Complete content management
- Visual database management
- User management
- Product inventory tracking

✅ **Responsive Design**
- Mobile-friendly interface
- Grid layouts
- Flexible navigation

## Troubleshooting

### Issue: ModuleNotFoundError when running migrations
**Solution**: Ensure virtual environment is activated
```bash
source venv/bin/activate
```

### Issue: Database locked error
**Solution**: Delete db.sqlite3 and run migrations again
```bash
rm db.sqlite3
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic
```

### Issue: Can't access admin panel
**Solution**: Ensure superuser was created
```bash
python manage.py createsuperuser
```

## Production Deployment

Before deploying to production:
1. Change SECRET_KEY in settings.py
2. Set DEBUG = False
3. Set ALLOWED_HOSTS properly
4. Use a production database (PostgreSQL recommended)
5. Set up environment variables for sensitive data
6. Configure static file serving (e.g., with Gunicorn/Nginx)
7. Enable CSRF protection properly
8. Set secure cookies and headers

## Support

For issues or questions:
- Email: info@toebeans.com
- Check Django documentation: https://docs.djangoproject.com/

---
TOEBEANS Backend v1.0
