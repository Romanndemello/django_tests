from django.shortcuts import render
from django.views import generic
from produto.models import Produto

class AddNewProduct(generic.CreateView):
    model = Produto
    fields = '__all__'

class GetListOfProducts(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()