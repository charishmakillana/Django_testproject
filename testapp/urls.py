from django.conf.urls.static import static
from django.urls import path

from TestProject import settings
from  . import views
urlpatterns = [
    path('', views.Userview, ''),
    path('images',views.display_images,name='non_images'),
    path('search/',views.search_name,name='search'),

]

