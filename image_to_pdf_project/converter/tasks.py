import logging
from celery import shared_task
from fpdf import FPDF
import os
from django.conf import settings

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def convert_images_to_pdf_task(self, file_paths):
    logger.info("Starting PDF conversion task...")
    
    if not file_paths:
        logger.warning("No files provided for conversion.")
        return "No files provided."

    pdf = FPDF()
    pdf.set_auto_page_break(0)

    for file_path in file_paths:
        logger.info(f"Processing file {file_path}")
        try:
            pdf.add_page()
            pdf.image(file_path, x=10, y=10, w=190)
        except Exception as e:
            logger.error(f"Error adding image {file_path} to PDF: {e}")
            return f"Error adding image {file_path} to PDF: {e}"

    pdf_output_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'output.pdf')

    try:
        logger.info(f"Ensuring directory exists: {os.path.dirname(pdf_output_path)}")
        os.makedirs(os.path.dirname(pdf_output_path), exist_ok=True)
        logger.info(f"Generating PDF file at: {pdf_output_path}")
        pdf.output(pdf_output_path)
        logger.info(f"PDF successfully created at {pdf_output_path}")
        return pdf_output_path
    except Exception as e:
        logger.error(f"Error creating PDF file: {e}")
        return f"Error creating PDF file: {e}"
