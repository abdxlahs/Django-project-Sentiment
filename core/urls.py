from django.urls import path
from .views import SentimentAnalysisView , HelloView

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze'),
    path('hello/', HelloView.as_view(), name='Hello'),
]
