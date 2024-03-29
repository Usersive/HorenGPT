from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('logout', views.logout, name='logout'),
  
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)