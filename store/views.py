from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Brand, Product, Category, BlogPost, UserProfile
from .forms import SignUpForm, LoginForm, UserProfileForm


def home(request):
    """Home page view"""
    featured_products = Product.objects.filter(is_featured=True)[:6]
    brands = Brand.objects.all()
    context = {
        'featured_products': featured_products,
        'brands': brands,
    }
    return render(request, 'store/index.html', context)


def signup(request):
    """User signup view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = SignUpForm()
    
    return render(request, 'store/signup.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                    return redirect('home')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    """User profile view"""
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'store/profile.html', context)


def shop(request):
    """Shop/products listing view"""
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    
    # Filter by brand
    brand_id = request.GET.get('brand')
    if brand_id:
        products = products.filter(brand_id=brand_id)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'selected_brand': brand_id,
        'selected_category': category_id,
        'search_query': search_query,
    }
    return render(request, 'store/shop.html', context)


def product_detail(request, product_id):
    """Product detail view"""
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(
        brand=product.brand
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)


def brand_detail(request, brand_id):
    """Brand detail view"""
    brand = get_object_or_404(Brand, id=brand_id)
    products = brand.products.all()
    
    context = {
        'brand': brand,
        'products': products,
    }
    return render(request, 'store/brand_detail.html', context)


def category_view(request, category_name):
    """Category view (Men/Women etc)"""
    category = get_object_or_404(Category, name__iexact=category_name)
    products = category.products.all()
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/category.html', context)


def blog(request):
    """Blog listing view"""
    posts = BlogPost.objects.all()
    
    context = {
        'posts': posts,
    }
    return render(request, 'store/blog.html', context)


def blog_detail(request, post_id):
    """Blog post detail view"""
    post = get_object_or_404(BlogPost, id=post_id)
    related_posts = BlogPost.objects.exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'store/blog_detail.html', context)


def about_us(request):
    """About us page"""
    return render(request, 'store/aboutus.html')


def research(request):
    """Research page"""
    return render(request, 'store/research.html')
