from django.urls import path
from .views  import SentimentAnalysisView, HelloView, FileUploadView, UploadedFileViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("files", UploadedFileViewSet, basename="uploadedfile")

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze'),
    path('hello/', HelloView.as_view(), name='Hello'),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
