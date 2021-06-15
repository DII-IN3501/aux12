from django.urls import path
from userApp.views import registerView, loginView, logoutView, auth, newuser

urlpatterns = [
    path('register/', registerView, name="register"),
    path('newuser/', newuser, name="newuser"),
    path('login/', loginView, name="login"),
    path('auth/', auth, name='auth'),
    path('logout/', logoutView, name='logout')
]
