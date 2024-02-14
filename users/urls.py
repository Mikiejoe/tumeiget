from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.search,name='home'),
    path('home/',views.home1,name='home'),
    path('stats/',views.getstats),
    path('add/',views.AddId.as_view()),
    path('add-details/',views.AddDetails.as_view()),
]
