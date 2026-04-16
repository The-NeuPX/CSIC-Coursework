# TOEBEANS Backend - Architecture Overview

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface (Frontend)                  │
│  13 HTML Templates + CSS in Django Templates                 │
│  (All your pages integrated with Django)                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Django View Layer (14 Views)                     │
│  home, signup, login, logout, profile                        │
│  shop, product_detail, brand_detail, category                │
│  blog, blog_detail, about_us, research                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           Django Model Layer (5 Models)                       │
│  Brand ◄─── Product ◄─── Category                           │
│  User  ◄─── UserProfile                                      │
│  User  ◄─── BlogPost                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
         ┌─────────────────────────┐
         │   SQLite Database       │
         │                         │
         │  - Brands              │
         │  - Categories          │
         │  - Products            │
         │  - Users               │
         │  - UserProfiles        │
         │  - BlogPosts           │
         │  - Sessions            │
         └─────────────────────────┘
```

## 🗺️ Site Map

```
┌─ http://localhost:8000/
│
├─ PUBLIC PAGES
│  ├─ / (homepage)
│  ├─ /shop/ (product catalog)
│  ├─ /product/<id>/ (product details)
│  ├─ /brand/<id>/ (brand showcase)
│  ├─ /category/<name>/ (Men/Women)
│  ├─ /blog/ (blog listing)
│  ├─ /blog/<id>/ (blog post)
│  ├─ /about/ (about page)
│  └─ /research/ (research page)
│
├─ AUTHENTICATION
│  ├─ /signup/ (new users)
│  ├─ /login/ (existing users)
│  ├─ /logout/ (end session)
│  └─ /profile/ (protected - login required)
│
└─ ADMIN PORTAL
   └─ /admin/ (dashboard)
      ├─ /admin/store/brand/ (manage brands)
      ├─ /admin/store/category/ (manage categories)
      ├─ /admin/store/product/ (manage products)
      ├─ /admin/store/blogpost/ (manage posts)
      ├─ /admin/store/userprofile/ (manage profiles)
      └─ /admin/auth/user/ (manage users)
```

## 📊 Data Flow Diagram

```
User Visits /shop/
│
├─ View: shop()
│  ├─ GET query params (brand, category, search)
│  ├─ Query: Product.objects.filter()
│  └─ Return: shop.html with context
│
├─ Template: shop.html (extends base.html)
│  ├─ Displays filters
│  ├─ Renders product grid
│  └─ Links to product_detail
│
└─ Database: Products table

User Clicks on Product
│
├─ View: product_detail(product_id)
│  ├─ Get product by ID
│  ├─ Get related products
│  └─ Return: product_detail.html
│
├─ Template: product_detail.html
│  ├─ Shows product image
│  ├─ Price, brand, stock
│  ├─ Related items grid
│  └─ Back to shop link
│
└─ Database: Product, Brand, Category tables
```

## 👤 User Journey

```
ANONYMOUS USER
│
├─ Lands on homepage (/)
│ └─ Sees featured products from database
│
├─ Browses shop (/shop/)
│ └─ Filters by brand/category
│ └─ Searches products
│
├─ Views product (/product/<id>/)
│ └─ Sees details, related items
│
├─ Clicks "Sign Up"
│ └─ Fills form (email, name, password)
│ └─ Submitted to signup view
│ └─ Validation: email unique? password strong?
│ └─ If valid: User + UserProfile created
│ └─ Logged in automatically
│
├─ Redirected to homepage
│ └─ Now sees "Welcome!" + profile/logout buttons
│
├─ Clicks profile
│ └─ Views /profile/
│ └─ Sees account info + form to edit
│
├─ Edits profile
│ └─ Updates address, phone, picture
│ └─ Saved to UserProfile in database
│
└─ Later: Logout, then Login
   └─ Login view: Email + password
   └─ Validated against password hash
   └─ Session created
   └─ Redirected to homepage
```

## 🛠️ Admin Workflow

```
ADMIN USER
│
├─ Logs into /admin/
│ └─ Session created for superuser
│
├─ Manages Products (/admin/store/product/)
│ ├─ Add Product
│ │  └─ Form: name, brand, category, price
│ │  └─ Upload image
│ │  └─ Set stock, featured flag
│ │  └─ Save to database
│ ├─ Edit Product
│ │  └─ Search or browse list
│ │  └─ Modify fields
│ │  └─ Update in database
│ └─ Delete Product
│    └─ Remove from database
│
├─ Manages Brands (/admin/store/brand/)
│ ├─ Add new brands
│ ├─ Edit descriptions
│ └─ View all products by brand
│
├─ Publishes Blog Posts (/admin/store/blogpost/)
│ ├─ Create article
│ ├─ Upload featured image
│ ├─ Auto-set to current user as author
│ └─ Appears on /blog/
│
├─ Views Users (/admin/store/userprofile/)
│ ├─ See all registered users
│ ├─ View addresses
│ ├─ Check registration dates
│ └─ Edit user profiles
│
└─ Analytics & Settings
   └─ View signup history
   └─ Track product inventory
   └─ Monitor blog traffic
```

## 🔐 Authentication Flow

```
SIGNUP FLOW
┌──────────────────────────────┐
│  User fills signup form       │
│  - Email                      │
│  - First/Last name            │
│  - Password                   │
└──────────────────┬───────────┘
                   │
                   ▼
       ┌───────────────────────┐
       │ Form Validation       │
       │ - Email format?       │
       │ - Email unique?       │
       │ - Password strength?  │
       │ - Match confirmation? │
       └─────────┬─────────────┘
                 │
         ┌─────────────┐
         │ Valid?      │
         ├──YES───────┤
         │            │ NO
         ▼            ▼
    Create User  Error Message
    Create Profile Shown
    Hash Password
    Create Session
    Login User
         │        Re-display
         ▼        Form with
    Redirect /    Errors
    Homepage
```

## 🗄️ Database Relationships

```
Brand (1) ──────── (*) Product
 │name              │name
 │description       │price
 │                  │brand_id (FK)
 │                  │category_id (FK)
 │
Category (1) ────── (*)
 │name
 │description

User (1:1) UserProfile
 │username  │phone
 │email     │address
 │password  │user_id (FK)
 │
User (1) ──────── (*) BlogPost
 │               │title
 │               │content
 │               │author_id (FK)
```

## 📁 Template Hierarchy

```
base.html (Master)
│
├─ header (navigation)
│  └─ logo, nav links, auth buttons
├─ main content block (extends in child)
├─ footer
│
├─ index.html
│  └─ featured products
│  └─ brands showcase
│
├─ shop.html
│  └─ filters (brand, category)
│  └─ product grid
│
├─ product_detail.html
│  └─ product image
│  └─ price, stock
│  └─ related products
│
├─ blog.html
│  └─ blog post listing
│  └─ article previews
│
├─ signup.html
│  └─ registration form
│
├─ login.html
│  └─ login form
│
├─ profile.html
│  └─ user info display
│  └─ edit form
│
└─ Other pages...
   └─ brand_detail.html
   └─ category.html
   └─ blog_detail.html
   └─ aboutus.html
   └─ research.html
```

## 🎯 URL Resolution Process

```
User visits: http://localhost:8000/product/5/
│
├─ Django URLconf (toebeans/urls.py)
│  └─ / → store.urls
│
├─ App URLconf (store/urls.py)
│  └─ matches: product/<id>/ → product_detail view
│
├─ View: product_detail(id=5)
│  ├─ Query: Product.objects.get(id=5)
│  ├─ Query: Product.objects.filter(brand=obj.brand)
│  └─ Context: {'product': obj, 'related': [...]}
│
├─ Template: product_detail.html
│  ├─ Renders with context
│  ├─ Displays product info
│  └─ Loops through related products
│
└─ Response: HTML sent to browser
```

## 🔄 Request/Response Cycle

```
┌─────────────┐
│   Browser   │
│             │
│ User clicks │
│   /shop/    │
└──────┬──────┘
       │
       │ HTTP GET /shop/?brand=1
       ▼
┌─────────────────────────────┐
│     Django Middleware       │
│ - CSRF check                │
│ - Session load              │
│ - User authentication       │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   URL Router (urls.py)      │
│ /shop/ → shop() view        │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   View Function (views.py)  │
│ def shop(request):          │
│   products = Product...()   │
│   return render(...)        │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   Template (HTML)           │
│ shop.html rendered with:    │
│ - products list             │
│ - filters form              │
│ - product cards             │
└──────────┬──────────────────┘
           │
           │ HTTP Response (HTML)
           ▼
┌─────────────┐
│   Browser   │
│             │
│ Renders     │
│ HTML page   │
└─────────────┘
```

## 🚀 Deployment Architecture

```
Development (Now)
├─ Django development server
├─ SQLite database
├─ DEBUG = True
└─ Auto-reload on file changes

Production (Later)
├─ Gunicorn (Python application server)
├─ Nginx (Reverse proxy, static files)
├─ PostgreSQL (Database)
├─ DEBUG = False
├─ HTTPS/SSL enabled
├─ Environment variables for secrets
└─ Static files collected and served by Nginx
```

## 📈 Scalability Notes

### Current Setup
- SQLite database (great for development)
- Development server (single process)
- Limited concurrent users (~10)

### To Scale to Production
1. **Database**: Migrate to PostgreSQL
2. **Server**: Use Gunicorn with multiple workers
3. **Web Server**: Use Nginx as reverse proxy
4. **Caching**: Add Redis for sessions/caching
5. **Static Files**: Serve from CDN or S3
6. **Load Balancing**: Use if multiple servers
7. **Monitoring**: Add logging and monitoring

---

## 🎓 Learning Path

1. **Basics**: Read README.md & DEPLOYMENT_SUMMARY.md
2. **Setup**: Follow SETUP_GUIDE.md
3. **Testing**: Test signup, login, products
4. **Admin**: Learn to use admin panel
5. **Customization**: Edit CSS, add more products
6. **Advanced**: Read INTEGRATION_GUIDE.md & Django docs

---

**Everything is connected and working as a complete system!** 🎉
