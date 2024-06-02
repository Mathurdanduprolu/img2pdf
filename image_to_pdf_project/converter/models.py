from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='temp/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)
