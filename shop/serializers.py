from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product, Article

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category_id']

class CategorySerializer(ModelSerializer):

    # Nous redéfinissons l'attribut 'product' qui porte le même nom que dans la liste des champs à afficher en lui
    # précisant un serializer paramétré à  'many=True' car les produits sont multiples pour une catégorie.
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product_id']
