from django.urls import path
from . import views

urlpatterns = [
    # Home & auth
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Shop & products
    path('shop/', views.shop, name='shop'),
    path('product/', views.product_by_file, name='product_by_file'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('brand/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('category/<str:category_name>/', views.category_view, name='category'),
    
    # Blog
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    
    # Info pages
    path('about/', views.about_us, name='about'),
    path('research/', views.research, name='research'),
]
