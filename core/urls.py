from django.urls import path
from .views import SentimentAnalysisView , HelloView ,FileUploadView

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze'),
    path('hello/', HelloView.as_view(), name='Hello'),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
