from django.urls import path
from .views import MainPageView, DetailView, home_redirect

urlpatterns = [
    path('<int:page_number>', MainPageView.as_view(), name='home'),
    path('product/<slug:product_slug>', DetailView.as_view(), name="product"),
    path('', home_redirect, name='from_home')]

