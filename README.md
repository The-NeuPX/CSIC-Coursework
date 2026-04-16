# TOEBEANS Django Backend - Quick Start Guide

## What's Been Created

I've created a complete Django backend for your TOEBEANS shoe shop website with the following components:

### ✅ Backend Infrastructure
- **Django Project**: `toebeans_backend/` - Production-ready Django project
- **Database Models**: Product, Brand, Category, User, UserProfile, BlogPost
- **Admin Panel**: Full-featured admin interface at `/admin/`
- **Authentication**: Email-based signup, login, and user profiles
- **Database**: SQLite (can be upgraded to PostgreSQL for production)

### ✅ User Features
- **Authentication System**
  - Email-based signup with password validation
  - Login/logout functionality
  - User profile management with contact information
  - Session management

- **Product Catalog**
  - Browse all products
  - Filter by brand and category
  - Search functionality
  - Product detail pages with related items
  - Featured products on homepage

- **Brand Pages**
  - Individual brand showcases
  - Brand-specific product listings

- **Blog System**
  - Blog post creation and viewing
  - Featured images
  - Author attribution
  - Related articles

### ✅ Admin Portal Features
- **Dashboard**: Manage all content from one place
- **Product Management**: Add, edit, delete products with inventory tracking
- **Brand Management**: Manage shoe brands
- **Category Management**: Men, Women, etc.
- **User Management**: View and manage user accounts
- **Blog Management**: Create and publish blog posts
- **User Profiles**: View customer information and addresses

## Project Structure

```
toebeans_backend/
├── manage.py                 # Django CLI
├── requirements.txt          # Dependencies
├── setup.sh                  # One-click setup script
├── SETUP_GUIDE.md           # Detailed setup instructions
├── toebeans/                 # Main Django project
│   ├── settings.py          # Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI config
└── store/                    # Main app
    ├── models.py            # Database models
    ├── views.py             # View logic (14 pages)
    ├── forms.py             # Authentication forms
    ├── admin.py             # Admin configuration
    ├── urls.py              # App URLs
    ├── templates/store/     # HTML templates
    │   ├── base.html        # Base template with navigation
    │   ├── index.html       # Homepage
    │   ├── shop.html        # Product listing
    │   ├── product_detail.html
    │   ├── brand_detail.html
    │   ├── category.html
    │   ├── blog.html        # Blog listing
    │   ├── blog_detail.html
    │   ├── login.html       # Login page
    │   ├── signup.html      # Registration
    │   ├── profile.html     # User profile
    │   ├── aboutus.html     # About page
    │   └── research.html    # Research page
    ├── static/store/
    │   └── css/
    │       └── base.css     # Complete styling
    └── management/commands/
        └── init_data.py     # Sample data initialization
```

## Quick Setup (5 Minutes)

### Step 1: Navigate to Backend Directory
```bash
cd /home/neupx/Downloads/Website/toebeans_backend
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
python manage.py migrate
```

### Step 5: Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts. Use an email like `admin@toebeans.com` and choose a password.

### Step 6: Load Sample Data (Optional)
```bash
python manage.py init_data
```

### Step 7: Start Server
```bash
python manage.py runserver
```

**Website**: http://localhost:8000  
**Admin Panel**: http://localhost:8000/admin/

## All URLs Available

### User Pages
- `http://localhost:8000/` - Home page with featured products
- `http://localhost:8000/shop/` - Full product catalog
- `http://localhost:8000/product/<id>/` - Product details
- `http://localhost:8000/brand/<id>/` - Brand showcase
- `http://localhost:8000/category/<name>/` - Category view (Men, Women)
- `http://localhost:8000/blog/` - Blog listing
- `http://localhost:8000/blog/<id>/` - Blog post details
- `http://localhost:8000/about/` - About Us page
- `http://localhost:8000/research/` - Research page

### Authentication
- `http://localhost:8000/signup/` - User registration
- `http://localhost:8000/login/` - User login
- `http://localhost:8000/logout/` - User logout
- `http://localhost:8000/profile/` - Edit profile (requires login)

### Admin Panel
- `http://localhost:8000/admin/` - Dashboard
- Manage: Products, Brands, Categories, Blog Posts, Users

## Database Models Explained

### Brand
```
- name (unique)
- description
- created_at (auto)
```

### Category
```
- name (Men, Women, etc.)
- description
```

### Product
```
- name
- brand (linked to Brand)
- category (linked to Category)
- price
- description
- image (optional)
- stock (quantity available)
- is_featured (shows on homepage)
- created_at, updated_at (auto)
```

### UserProfile
```
- user (linked to Django User)
- phone, address, city, state, zipcode
- profile_picture
- created_at (auto)
```

### BlogPost
```
- title
- content
- author (linked to User)
- featured_image
- created_at, updated_at
```

## Key Features

### Authentication ✅
- Email-based signup (automatically creates UserProfile)
- Password hashing with Django's built-in security
- Login/logout with session management
- Protected views (login required for profile)

### Admin Interface ✅
- Visual database management
- Searchable fields
- Filters (by brand, category, date)
- Bulk actions
- Read-only timestamps

### Product Management ✅
- Add/edit products with images
- Track inventory
- Mark as featured for homepage
- Filter by brand and category
- Search by name

### User Management ✅
- View all registered users
- Edit user information
- Manage user profiles with addresses
- Track registration dates

### Blog Management ✅
- Create articles with rich content
- Upload featured images
- Author attribution
- Publishing timeline

## Forms Included

### SignUp Form
- Email validation
- Password strength checking
- Password confirmation
- Nome fields (optional)
- Auto-creates UserProfile on signup

### Login Form
- Email-based authentication
- Password validation
- Error messages for invalid credentials

### User Profile Form
- Edit contact information
- Upload profile picture
- Update address details

## CSS Styling

Complete responsive CSS included:
- Mobile-first design
- Grid layouts for products
- Flexbox navigation
- Smooth transitions
- Professional color scheme (black, cyan, beige)
- Fully responsive (works on all devices)

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'django'`  
**Solution**: Ensure virtual environment is activated: `source venv/bin/activate`

**Problem**: Database errors  
**Solution**: Reset database: `rm db.sqlite3 && python manage.py migrate`

**Problem**: Can't log into admin  
**Solution**: Create superuser: `python manage.py createsuperuser`

**Problem**: Static files not loading  
**Solution**: `python manage.py collectstatic`

## Next Steps

1. **Add Your Logo**: Place logo image in `store/static/store/images/`
2. **Upload Products**: Go to admin → Products → Add products with images
3. **Write Blog Posts**: Admin → Blog Posts → Create articles
4. **Customize Colors**: Edit `store/static/store/css/base.css`
5. **Deploy**: Use Gunicorn + Nginx for production

## File Checklist

✅ `manage.py` - Django CLI  
✅ `requirements.txt` - Dependencies  
✅ `toebeans/settings.py` - Configuration  
✅ `toebeans/urls.py` - Main URL routing  
✅ `toebeans/wsgi.py` - WSGI config  
✅ `store/models.py` - Database models (5 models)  
✅ `store/views.py` - View logic (14 page views)  
✅ `store/forms.py` - 3 authentication forms  
✅ `store/admin.py` - Admin configuration  
✅ `store/urls.py` - App-level URL routing  
✅ `store/templates/` - 14 HTML templates  
✅ `store/static/css/base.css` - Complete styling  
✅ `store/management/commands/init_data.py` - Sample data loader  
✅ `SETUP_GUIDE.md` - Detailed documentation  

## Integration Notes

All original HTML/CSS from your frontend has been:
- Converted to Django templates
- Integrated with database models
- Connected to authentication system
- Styled with consistent CSS
- Made responsive and modern

The backend automatically:
- Creates user profiles on signup
- Manages sessions
- Handles form validation
- Protects sensitive views
- Logs users in/out
- Updates user information

## Production Deployment

Before deploying:
1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL (not SQLite)
5. Set up environment variables
6. Use Gunicorn + Nginx
7. Enable HTTPS
8. Set secure cookies

---

**Your TOEBEANS backend is now ready to use!**

For detailed instructions, see `SETUP_GUIDE.md`
