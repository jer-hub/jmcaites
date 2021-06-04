from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'students'
urlpatterns = [
    path('',views.index, name='index'),
    path('search/', views.search, name='search'),
    path('add/',views.add, name='add'),
    path('add/process/', views.processadd, name='process_add'),
    path('<int:profile_id>/details', views.details, name='details'),
    path('<int:profile_id>/delete', views.delete_user, name='delete_user'),
    path('<int:profile_id>/edit', views.edit_user, name='edit_user'),
    path('<int:profile_id>/process', views.process_edit, name='process_edit'),
    path('addcomment/', views.addcomment, name='addcomment'),
] + static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL,
    document_root = settings.STATIC_ROOT)