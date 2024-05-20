from django.contrib import admin
from django.urls import path,include
from reciepe_app import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("", views.home, name="home"),
    path('home',views.index,name="index"),
    path('add-reciepe',views.add_reciepe,name="add_reciepe"),
    path('delete-reciepe/<id>/',views.delete_reciepe,name="delete_reciepe"),
    path('update-reciepe/<id>/',views.update_reciepe,name="update_reciepe"),
    path('register-page',views.register_page,name="register_page"),
    path('login-page',views.login_page,name="login_page"),
    path('logout-page',views.logout_page,name="logout_page"),
    path('reciepe-view/<id>/',views.reciepe_view,name='reciepe_view')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()