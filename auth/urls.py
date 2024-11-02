from django.urls import path
from .views import login_view,logout_view,Form_view


urlpatterns = [
    path('login/',login_view.as_view(),name='login'),
    path('logout/',logout_view,name='logout'), #logout view has an attribute next page where users wil be sent after logging out
    path('signup/',Form_view.as_view(),name='signup')
]