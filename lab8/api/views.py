from django.http.response import HttpResponse, JsonResponse
from api.models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    categories_tojson = [category.to_json() for category in categories]

    return JsonResponse(categories_tojson, safe=False)


def get_category(request, pk=None):
    try:
        category = Category.objects.all().get(id=pk)
        return JsonResponse(category.to_json(), safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'Category does not exist'}, safe=False)


def get_products(request):
    products = Product.objects.all()
    products_tojson = [product.to_json() for product in products]
    return JsonResponse(products_tojson, safe=False)


def get_product(request, pk=None):
    try:
        product = Product.objects.all().get(id=pk)
        return JsonResponse(product.to_json(), safe=False)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'Product does not exist'}, safe=False)


def get_products_by_category(request, pk=None):
    products = Product.objects.all().filter(category=pk)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)