from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.search,name='search'),
    path('stats/',views.getstats,name='stats'),
    path('stats/station/',views.getstats,name='station stats'),
    path('ids/',views.get_ids,name='ids'),
    path('add/',views.addid,name='add'),
    # path('add-details/',views.AddDetails.as_view(),name='add-details'),
    # path('user-details/',views.getuserdetails,name='user-details'),
    path('pick/',views.pick,name='pick'),
    path("add-details/",views.add_details,name="add-testing"),
    path('recent/',views.get_recent,name="recent"),
]
