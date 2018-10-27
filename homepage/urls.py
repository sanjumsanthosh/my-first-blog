
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.main_page),
    # path('add_post',views.login)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
