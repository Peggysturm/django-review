from django.urls import path
from .views import MainPageView, DetailView

urlpatterns = [
    path('<int:page_number>', MainPageView.as_view(), name='home'),
    path('product/<slug:product_slug>', DetailView.as_view(), name="product")]

