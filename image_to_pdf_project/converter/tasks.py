import logging
from celery import shared_task
from fpdf import FPDF
from .models import Image, PDF
import os
from django.conf import settings

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def convert_images_to_pdf(self):

    logger.info("Starting PDF conversion task...")
    images = Image.objects.all()

    if not images.exists():
        logger.warning("No images found for conversion.")
        return "No images found."

    pdf = FPDF()
    pdf.set_auto_page_break(0)

    for image in images:
        logger.info(f"Processing image {image.image.path}")
        try:
            pdf.add_page()
            pdf.image(image.image.path, x=10, y=10, w=190)
        except Exception as e:
            logger.error(f"Error adding image {image.image.path} to PDF: {e}")
            return f"Error adding image {image.image.path} to PDF: {e}"

    pdf_output_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'output.pdf')

    try:
        logger.info(f"Ensuring directory exists: {os.path.dirname(pdf_output_path)}")
        os.makedirs(os.path.dirname(pdf_output_path), exist_ok=True)
        logger.info(f"Generating PDF file at: {pdf_output_path}")
        pdf.output(pdf_output_path)
        PDF.objects.create(pdf_file='pdfs/output.pdf')  # Save relative path in DB
        logger.info(f"PDF successfully created at {pdf_output_path}")
        return pdf_output_path
    except Exception as e:
        logger.error(f"Error creating PDF file: {e}")
        return f"Error creating PDF file: {e}"



@shared_task(bind=True)
def simple_task(self):
    logger.info("Simple task executed successfully.")
    return "Simple task executed successfully."