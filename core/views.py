from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .ai_model import analyze_text , hello


class SentimentAnalysisView(APIView):
    def post(self, request):
        user_input = request.data.get("text")
        if not user_input:
            return Response({"error": "Text input is required"}, status=400)

        # Process the input through AI logic
        result = analyze_text(user_input)
        return Response(result)
    
class HelloView(APIView):
    def post(self, request):
        user_input = request.data.get("text")
        if not user_input:
            return Response({"error": "Text input is required"}, status=400)

        # Process the input through AI logic
        result = hello(user_input)
        return Response(result)
