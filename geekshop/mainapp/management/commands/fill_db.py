import json
from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategory


def load_from_json(file_name):
    with open(file_name, mode='r',encoding='utf-8') as read_file:
        return json.load(read_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            current_cat = category.get('fields')
            current_cat['id'] = category.get('pk')
            new_cat = ProductCategory(**current_cat)
            new_cat.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            current_prod = product.get('fields')
            category = current_prod.get('category')
            my_category = ProductCategory.objects.get(id=category)
            current_prod['category'] = my_category
            new_cat = Product(**current_prod)
            new_cat.save()