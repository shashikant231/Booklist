from django.urls import path,include
from . import views

urlpatterns = [
    path('detail/',views.booklist,name='index'),
    path('add/',views.booklist_post,name='add'),
    path('searchbyname/',views.searchbynameview,name='searchbyname'),

]