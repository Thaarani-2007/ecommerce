 
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('newitem/',views.newitem,name='newitem'),
    path('browse/',views.browse,name='browse'),
    path('login/',views.login,name='login'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('edit/<slug>',views.edit,name='edit'),
    # path('latestproducts/',views.LatestProductsList.as_view,name='latestproducts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

