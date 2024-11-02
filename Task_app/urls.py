from django.urls import path
from .views import task_list,detail_view,update_view,create_view,delete_view
urlpatterns = [
    path('',task_list.as_view(),name='home'),
    path('detail/<pk>',detail_view.as_view(),name='detail'),
    path('update/<pk>',update_view.as_view(),name='update'),
    path('add/',create_view.as_view(),name="create"),
    path('delete/<pk>',delete_view.as_view(),name='delete')
]
