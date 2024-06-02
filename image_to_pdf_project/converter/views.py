from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import Image, PDF
from .tasks import convert_images_to_pdf
from django.http import HttpResponse
import time
import logging

logger = logging.getLogger(__name__)

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info("Image uploaded successfully, triggering PDF conversion task...")
            convert_images_to_pdf.delay()  # Trigger Celery task
            return redirect('pdf_generation_in_progress')
        else:
            logger.warning("Form is not valid.")
    else:
        form = ImageUploadForm()
    return render(request, 'converter/upload.html', {'form': form})

def pdf_generation_in_progress(request):
    logger.info("Rendering PDF generation in progress page...")
    return render(request, 'converter/pdf_generation_in_progress.html')

def get_generated_pdf(request):
    logger.info("Attempting to retrieve generated PDF...")
    time.sleep(10)  # Adjust this to the realistic time needed for the task
    try:
        latest_pdf = PDF.objects.latest('created_at')
        if latest_pdf:
            logger.info(f"Redirecting to PDF at {latest_pdf.pdf_file.url}")
            return redirect(latest_pdf.pdf_file.url)
        else:
            logger.warning("No PDF found, generation still in progress.")
            return HttpResponse("PDF generation is still in progress. Please try again later.")
    except PDF.DoesNotExist:
        logger.warning("No PDF found in the database.")
        return HttpResponse("No PDF found. Please try again later.")
