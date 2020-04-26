from django.urls import path
from .read import fetch_data
from .views import gen_graph
urlpatterns = [
       path('add_data/', fetch_data),
       path('home/',gen_graph),
]
