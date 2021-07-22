from django.conf.urls import url
from .views import PhotoUploadView

urlpatterns = [
    url(r'^images', PhotoUploadView.as_view())
]