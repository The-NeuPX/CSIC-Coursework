from django.contrib import admin
from .models import Brand, Category, Product, UserProfile, BlogPost

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'stock', 'is_featured']
    list_filter = ['brand', 'category', 'is_featured', 'created_at']
    search_fields = ['name', 'brand__name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'brand', 'category', 'price')
        }),
        ('Details', {
            'fields': ('description', 'image', 'stock', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'created_at']
    search_fields = ['user__username', 'phone', 'city']
    readonly_fields = ['created_at']
    fieldsets = (
        ('User', {
            'fields': ('user', 'profile_picture')
        }),
        ('Contact Information', {
            'fields': ('phone',)
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'zipcode')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'author', 'featured_image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
