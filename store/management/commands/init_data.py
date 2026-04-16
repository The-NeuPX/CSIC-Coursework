from django.core.management.base import BaseCommand
from store.models import Brand, Category, Product, BlogPost
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Initialize the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Initializing database...')

        # Create categories
        categories = [
            {'name': 'Men'},
            {'name': 'Women'},
        ]

        for cat_data in categories:
            cat, created = Category.objects.get_or_create(name=cat_data['name'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat.name}'))

        # Create brands
        brands_data = [
            {'name': 'Nike', 'description': 'Premium athletic footwear and sports shoes'},
            {'name': 'Adidas', 'description': 'Quality sports shoes and athletic wear'},
            {'name': 'Puma', 'description': 'Performance shoes combining style and comfort'},
            {'name': 'Prada', 'description': 'Luxury Italian footwear'},
            {'name': 'Dior', 'description': 'Elegant designer shoes'},
            {'name': 'Louboutin', 'description': 'Iconic luxury heels with red soles'},
            {'name': 'Jimmy Choo', 'description': 'Premium designer footwear'},
            {'name': 'Skechers', 'description': 'Comfortable casual and athletic shoes'},
        ]

        for brand_data in brands_data:
            brand, created = Brand.objects.get_or_create(
                name=brand_data['name'],
                defaults={'description': brand_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created brand: {brand.name}'))

        # Create sample products
        men_category = Category.objects.get(name='Men')
        women_category = Category.objects.get(name='Women')
        
        sample_products = [
            {'name': 'Air Max Pro', 'brand_name': 'Nike', 'category_name': 'Men', 'price': 129.99, 'stock': 50, 'is_featured': True},
            {'name': 'Ultraboost 22', 'brand_name': 'Adidas', 'category_name': 'Men', 'price': 149.99, 'stock': 40, 'is_featured': True},
            {'name': 'RS-X Sneaker', 'brand_name': 'Puma', 'category_name': 'Men', 'price': 89.99, 'stock': 30, 'is_featured': False},
            {'name': 'Prada Loafer', 'brand_name': 'Prada', 'category_name': 'Men', 'price': 850.00, 'stock': 10, 'is_featured': False},
            {'name': 'Air Force 1 Womens', 'brand_name': 'Nike', 'category_name': 'Women', 'price': 119.99, 'stock': 45, 'is_featured': True},
            {'name': 'Boost Womens', 'brand_name': 'Adidas', 'category_name': 'Women', 'price': 139.99, 'stock': 35, 'is_featured': False},
            {'name': 'Louboutin Heel', 'brand_name': 'Louboutin', 'category_name': 'Women', 'price': 950.00, 'stock': 5, 'is_featured': True},
        ]

        for prod_data in sample_products:
            try:
                category = Category.objects.get(name=prod_data['category_name'])
                brand = Brand.objects.get(name=prod_data['brand_name'])
                
                product, created = Product.objects.get_or_create(
                    name=prod_data['name'],
                    brand=brand,
                    defaults={
                        'category': category,
                        'price': prod_data['price'],
                        'stock': prod_data['stock'],
                        'is_featured': prod_data['is_featured'],
                        'description': f'Premium {prod_data["brand_name"]} footwear'
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            except (Category.DoesNotExist, Brand.DoesNotExist):
                pass

        # Create sample blog post
        try:
            admin_user = User.objects.first()
            if admin_user:
                post, created = BlogPost.objects.get_or_create(
                    title='Welcome to TOEBEANS Blog',
                    defaults={
                        'content': 'Welcome to the TOEBEANS blog! Stay tuned for the latest footwear trends, tips, and insights.',
                        'author': admin_user
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS('Created sample blog post'))
        except:
            pass

        self.stdout.write(self.style.SUCCESS('Database initialization complete!'))
