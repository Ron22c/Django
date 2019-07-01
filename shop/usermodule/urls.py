from django.conf.urls import url
from usermodule import views

app_name= 'usermodule'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^user_login', views.user_login, name = 'user_login')
]
