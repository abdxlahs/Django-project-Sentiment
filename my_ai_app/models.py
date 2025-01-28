from django.db import models

class UserInput(models.Model):
    input_text = models.TextField()
    prediction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
