from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    
    url(r'^kitchenware$', display_kitchenware, name='display_kitchenware'),
    url(r'^chicken$', display_chicken, name='display_chicken'),
    
    url(r'^add_kitchenware$', add_kitchenware, name='add_kitchenware'),
    url(r'^add_chicken$', add_chicken, name='add_chicken'),
    
    
    url(r'^kitchenware/edit_item/(?P<pk>\d+)$', edit_kitchenware, name="edit_kitchenware"),
    url(r'^chicken/edit_item/(?P<pk>\d+)$', edit_chicken, name="edit_chicken"),

    url(r'^kitchenware/delete/(?P<pk>\d+)$', delete_kitchenware, name="delete_kitchenware"),
    url(r'^chicken/delete/(?P<pk>\d+)$', delete_chicken, name="delete_chicken"),
   

    
]
