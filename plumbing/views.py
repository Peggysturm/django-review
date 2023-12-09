from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Plumbing
from .parser import parser

class MainPageView(ListView):
    template_name = "index.html"
    model = Plumbing
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        parser("https://smauro.ru/catalog/bytovaya_santekhnika/")
        queryset = super().get_queryset()
        return queryset
    

class DetailView(DetailView):
    model = Plumbing
    template_name = "plumbing_detail.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'