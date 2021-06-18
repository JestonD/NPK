from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import Upload, HomeView, CustomLoginView, RegisterView, DeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('',HomeView.as_view(),name='home'),
     path('register/', RegisterView.as_view(),name='register'),
     path('login/', CustomLoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
     path('upload/', Upload.as_view(),name='upload'),
     path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    