from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('AddCategory',views.add_category,name='add_category'),    
    path('imageupload',views.image_upload,name='image_upload'),
    path('gallery',views.gallery,name='gallery'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
