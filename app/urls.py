from django.urls import path,re_path
from .views import SellView,RentView,DetailSellFiles,DetailRentFiles

urlpatterns = [
    # The home page
    path('sell',SellView.as_view(),name='sell'),
    path('rent',RentView.as_view(),name='rent'),
    # path('create',CreateFileView.as_view(),name='create'),
    path('sell/<int:pk>',DetailSellFiles.as_view(),name="detsell"),
    path('rent/<int:pk>',DetailRentFiles.as_view(),name="detrent"),
     path('',SellView.as_view(),name='home'),
    # path('profile', views.profile, name='profile'),
    # path('contact', views.contact, name='contact'),
    # path('search',views.search,name='search'),
    # path('files', items.as_view(), name='files'),
    # path('file_detail/<int:id>/',views.items_detail,name='file_detail'),
]