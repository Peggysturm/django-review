from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Plumbing
from for_parser.parser import parser

class MainPageView(ListView):
    template_name = "index.html"
    model = Plumbing
    context_object_name = "products"
    page_number_kwarg = "page_number"

    def get_queryset(self) -> QuerySet[Any]:
        page_number = self.kwargs[self.page_number_kwarg]
        if page_number:
            queryset = parser("https://smauro.ru/catalog/bytovaya_santekhnika/", "all", page_number)
        else:
            queryset = parser("https://smauro.ru/catalog/bytovaya_santekhnika/", "all", 0)

        sort = self.request.GET.get('sort')

        if sort == 'many':
            queryset = sorted(queryset, key=lambda product: product.details.raiting, reverse=True)  
        elif sort == 'little':
            queryset = sorted(queryset, key=lambda product: product.details.raiting)  
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        page_number = self.kwargs[self.page_number_kwarg]
        context = super().get_context_data(**kwargs)
        sort_filter = self.request.GET.get('sort')
        context['page_number'] = page_number
        context['sort_filter'] = sort_filter if sort_filter else ''

        return super().get_context_data(**kwargs)
    

class DetailView(DetailView):
    model = Plumbing
    template_name = "plumbing_detail.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'