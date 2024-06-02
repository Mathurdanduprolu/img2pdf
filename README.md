# Image to PDF Converter with Django, Celery, and Redis

## Overview

This project demonstrates how to build an Image to PDF Converter web application using Django, Celery, and Redis. Users can upload images, which are then converted to a PDF in the background, ensuring a seamless and responsive experience.

## Features

- **Asynchronous Processing**: Uses Celery to handle background tasks, ensuring the main application remains responsive.
- **Scalability**: Capable of handling multiple file conversion requests simultaneously.
- **User-Friendly**: Provides a smooth and quick interaction for users by offloading heavy tasks to Celery.

## Requirements

- Python 3.x
- Django 3.x
- Celery 5.x
- Redis 6.x
- FPDF 1.x
- Tailwind CSS

## Installation
-Steps to run are written in the blog <https://medium.com/@mathur.danduprolu/building-an-image-to-pdf-converter-with-django-celery-and-redis-2f33506d5956>
