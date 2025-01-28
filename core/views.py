from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .ai_model import analyze_text , hello
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import UploadedFile
from .serializers import UploadedFileSerializer  ,ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product



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

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()

            # Process the file (e.g., parse CSV or perform some operation)
            file_path = file_instance.file.path
            result = f"File {file_path} has been successfully uploaded and processed."

            return Response({"message": result})
        return Response(file_serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer