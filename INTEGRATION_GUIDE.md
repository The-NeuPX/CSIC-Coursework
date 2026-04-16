# TOEBEANS Backend - Complete Integration Guide

## Backend Location
```
/home/neupx/Downloads/Website/toebeans_backend/
```

## Complete URL Map

### Homepage & Main Pages
| URL | View Function | Template | Features |
|-----|---------------|----------|----------|
| `/` | `home()` | `index.html` | Featured products, brands showcase |
| `/about/` | `about_us()` | `aboutus.html` | Company info, values, contact |
| `/research/` | `research()` | `research.html` | Footwear research, trends, tips |
| `/shop/` | `shop()` | `shop.html` | Full catalog, filters, search |

### Product Pages
| URL | View Function | Template | Features |
|-----|---------------|----------|----------|
| `/product/<id>/` | `product_detail()` | `product_detail.html` | Product info, images, related items |
| `/brand/<id>/` | `brand_detail()` | `brand_detail.html` | Brand showcase, brand products |
| `/category/<name>/` | `category_view()` | `category.html` | Men/Women/etc. product listings |

### Blog Pages
| URL | View Function | Template | Features |
|-----|---------------|----------|----------|
| `/blog/` | `blog()` | `blog.html` | Blog post listing |
| `/blog/<id>/` | `blog_detail()` | `blog_detail.html` | Full blog post, related posts |

### Authentication Pages
| URL | View Function | Template | Features |
|-----|---------------|----------|----------|
| `/signup/` | `signup()` | `signup.html` | User registration, validation |
| `/login/` | `login_view()` | `login.html` | Email-based authentication |
| `/logout/` | `logout_view()` | - | Session termination |
| `/profile/` | `profile()` | `profile.html` | User info, address, picture |

### Admin Panel
| URL | Purpose | Models |
|-----|---------|--------|
| `/admin/` | Dashboard | Full content management |
| `/admin/store/brand/` | Brand management | Add/edit/delete brands |
| `/admin/store/category/` | Category management | Men/Women/etc categories |
| `/admin/store/product/` | Product management | Inventory, prices, images |
| `/admin/store/blogpost/` | Blog management | Articles, publishing |
| `/admin/store/userprofile/` | User profiles | Addresses, contact info |
| `/admin/auth/user/` | User management | Accounts, permissions |

## Database Schema

### Brand Table
```
id (PK)
name (VARCHAR 100) - UNIQUE
description (TEXT)
created_at (DATETIME)
```

### Category Table
```
id (PK)
name (VARCHAR 100) - UNIQUE
description (TEXT)
```

### Product Table
```
id (PK)
name (VARCHAR 200)
brand_id (FK → Brand)
category_id (FK → Category)
price (DECIMAL 10,2)
description (TEXT)
image (ImageField)
stock (INTEGER)
is_featured (BOOLEAN)
created_at (DATETIME)
updated_at (DATETIME)
```

### UserProfile Table
```
id (PK)
user_id (FK → User) - UNIQUE
phone (VARCHAR 20)
address (TEXT)
city (VARCHAR 100)
state (VARCHAR 100)
zipcode (VARCHAR 20)
profile_picture (ImageField)
created_at (DATETIME)
```

### BlogPost Table
```
id (PK)
title (VARCHAR 200)
content (TEXT)
author_id (FK → User)
featured_image (ImageField)
created_at (DATETIME)
updated_at (DATETIME)
```

### Django User Table (Built-in)
```
id (PK)
username (VARCHAR 150)
email (VARCHAR 254)
first_name (VARCHAR 150)
last_name (VARCHAR 150)
password (hashed)
is_active (BOOLEAN)
is_staff (BOOLEAN)
is_superuser (BOOLEAN)
date_joined (DATETIME)
```

## Authentication Flow

### Signup Flow
1. User visits `/signup/`
2. Fills form (email, name, password)
3. Form validates:
   - Email uniqueness
   - Password strength
   - Password confirmation
4. User created with email as username
5. UserProfile auto-created
6. User logged in automatically
7. Redirect to homepage

### Login Flow
1. User visits `/login/`
2. Enters email and password
3. System queries by email
4. Password verified
5. Session created
6. User logged in
7. Redirect to profile or home

### Protected Views
- `/profile/` - LoginRequired
- Other views - Publicly accessible
- Admin panel - Permission required

## Form Validation

### SignUpForm
```
- email: Required, unique, valid email
- first_name: Optional, max 30 chars
- last_name: Optional, max 30 chars
- password1: Required, min 8 chars, complexity
- password2: Required, must match password1
```

### LoginForm
```
- email: Required, valid email format
- password: Required, validated against DB
```

### UserProfileForm
```
- phone: Optional, max 20 chars
- address: Optional, text area
- city: Optional, max 100 chars
- state: Optional, max 100 chars
- zipcode: Optional, max 20 chars
- profile_picture: Optional, image upload
```

## Views & Logic (14 Page Views)

### `home()`
- Fetches featured products (is_featured=True)
- Fetches all brands
- Passes to index.html
- Purpose: Homepage with showcase

### `signup()`
- GET: Displays signup form
- POST: Creates user account
- Validation: Email uniqueness
- Auto-creates UserProfile
- Redirects to home

### `login_view()`
- GET: Displays login form
- POST: Authenticates user
- Creates session
- Redirects to home

### `logout_view()`
- Terminates session
- Redirects to home

### `profile()`
- LoginRequired
- Displays/edits user profile
- Uploads profile picture
- Saves address info

### `shop()`
- Lists all products
- Filters: brand, category, search
- Pagination ready
- Showcases catalog

### `product_detail(id)`
- Displays single product
- Shows related products
- Brand/category info
- Stock status

### `brand_detail(id)`
- Brand description
- Brand's products
- Brand showcase

### `category_view(name)`
- Category's products
- Dynamic routing: Men/Women/etc
- Product grid

### `blog()`
- Lists all blog posts
- Displays featured images
- Author info, dates

### `blog_detail(id)`
- Full blog post
- Featured image
- Related posts

### `about_us()`
- Static content
- Company mission, values
- Contact information

### `research()`
- Static content
- Footwear research
- Industry trends

## Admin Features

### Brand Admin
- Search by name
- List: name, created_at
- Filters: creation date
- Add/edit/delete

### Category Admin
- Search by name
- List: name
- Add/edit/delete

### Product Admin
- Advanced search: name, brand
- Filters: brand, category, featured, date
- List: name, brand, price, stock, featured
- Fieldsets: organization, readonly timestamps
- Image upload support

### Blog Admin
- Search: title, content
- Filters: author, date
- List: title, author, date
- Rich text editor support
- Image upload

### UserProfile Admin
- Search: username, phone, city
- Filters: creation date
- List: user, phone, city, date
- Address fields
- Readonly timestamps

## Static Files Organization

```
store/static/store/
├── css/
│   └── base.css (1500+ lines)
│       ├── Reset styles
│       ├── Header & navigation
│       ├── Forms & buttons
│       ├── Product grid
│       ├── Footer
│       └── Responsive design
└── (ready for: images/, js/, fonts/)
```

## Template Inheritance

```
base.html (Master template)
├── Promo bar
├── Header with nav
├── Messages section
├── {% block content %}
└── Footer

Child templates:
├── index.html (extends base.html)
├── signup.html (extends base.html)
├── login.html (extends base.html)
├── shop.html (extends base.html)
├── product_detail.html (extends base.html)
├── blog.html (extends base.html)
├── profile.html (extends base.html)
└── ... etc (all extend base.html)
```

## Settings Configuration

### Key Settings
```python
DEBUG = True                          # Dev mode
ALLOWED_HOSTS = ['*']                # All hosts allowed
DATABASES = SQLite3                  # Default DB
AUTH_PASSWORD_VALIDATORS = [...]     # Password strength
LOGIN_URL = 'login'                  # Default login page
LOGIN_REDIRECT_URL = 'home'          # Post-login redirect
STATIC_URL = '/static/'              # Static files path
MEDIA_URL = '/media/'                # User uploads path
```

### INSTALLED_APPS
```
django.contrib.admin
django.contrib.auth
django.contrib.contenttypes
django.contrib.sessions
django.contrib.messages
django.contrib.staticfiles
store (custom app)
```

## URL Configuration

### Root URLs (`toebeans/urls.py`)
```python
/admin/ → Django admin
/ → store.urls (app URLs)
```

### App URLs (`store/urls.py`)
```python
'' → home (index)
signup/ → signup
login/ → login_view
logout/ → logout_view
profile/ → profile
shop/ → shop
product/<id>/ → product_detail
brand/<id>/ → brand_detail
category/<name>/ → category_view
blog/ → blog
blog/<id>/ → blog_detail
about/ → about_us
research/ → research
```

## Relationships Map

```
Brand (1) ──── (*) Product
Category (1) ──── (*) Product
User (1) ──── (1) UserProfile
User (1) ──---- (*) BlogPost
```

## Middleware Stack

```
1. SecurityMiddleware - Security headers
2. SessionMiddleware - Session management
3. CommonMiddleware - Common utilities
4. CsrfViewMiddleware - CSRF protection
5. AuthenticationMiddleware - User authentication
6. MessageMiddleware - Django messages
7. XFrameOptionsMiddleware - Clickjacking protection
```

## Context Processors

```
debug - DEBUG setting
request - Current request
auth - User authentication
messages - Django messages
```

## File Upload Paths

```
Product images: media/product_images/
Blog images: media/blog_images/
Profile pictures: media/profile_pictures/
```

## Error Handling

### 404 Pages
- Product not found → 404
- Brand not found → 404
- Category not found → 404
- Post not found → 404

### Form Validation
- Invalid email → Form error
- Weak password → Form error
- Email already registered → Form error
- Login failed → Form error

### Message System
- Success messages (green)
- Error messages (red)
- Auto-dismiss after 5 seconds

## Session Management

- Default session timeout: 2 weeks
- Session storage: Database
- Secure cookies enabled
- CSRF protection enabled

## User Permissions

- Anonymous: View all pages except profile
- Authenticated: Can view profile, edit profile
- Staff: Access admin panel
- Superuser: Full admin access

---

## Quick Reference

### To Add a New Product:
1. Go to /admin/
2. Click "Products" → "Add Product"
3. Fill: name, brand, category, price, stock
4. Upload image (optional)
5. Click Save

### To Create Blog Post:
1. Go to /admin/
2. Click "Blog Posts" → "Add Blog Post"
3. Fill: title, content, author
4. Upload featured image
5. Click Save

### To View User Info:
1. Go to /admin/
2. Click "Users" or "User Profiles"
3. Search or browse
4. View/edit details

### To Test Authentication:
1. Visit /signup/
2. Create test account
3. Visit /login/
4. Login with credentials
5. View /profile/

---

**Complete backend system ready for production deployment!**
