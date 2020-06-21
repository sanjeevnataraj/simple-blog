"""simpleblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('signup/',views.signupview.as_view(),name='signup'),
	path('login/',views.Loginview.as_view(),name="login"),
	path('logout/',views.user_logout,name="logout"),
    path('add/article/',views.add_edit_article,name='add-article'),
    path('validate/user/',views.validate_user,name='validate'),
    path('article/<int:pk>',views.articleView,name='article_view'),
    url(r'^$', views.homepage, name='home'),
    path('archive/', views.ArchivePage.as_view(), name='archive'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact_page, name='contact'),
    path('category/<pk>', views.category, name='category'),
    url(r'^simple/', include('social_django.urls', namespace='social')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
