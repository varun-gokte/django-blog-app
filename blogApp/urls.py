from django.urls import path
from blogApp import views

app_name = 'blogApp'
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
    path('signup', views.signup_request, name="signup"),
    path('new', views.create_post, name='create'),
    path('article/<number>', views.display_post, name='display'),
    path('user/<name>', views.user_page, name="user"),
    path('change/<type>', views.change_details, name="change"),
    path('edit/<number>', views.update_post, name="update"),
    path('delete/<number>', views.delete_post, name="delete"),
]
