from django.urls import path
from .views import login_view,home,signup_view,logout_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]

