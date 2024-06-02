from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.image_upload_view, name='image_upload'),
    path('pdf-generation-in-progress/', views.pdf_generation_in_progress, name='pdf_generation_in_progress'),
    path('get-generated-pdf/', views.get_generated_pdf, name='get_generated_pdf'),
]
