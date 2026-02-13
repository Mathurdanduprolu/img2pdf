
# img2pdf – Image to PDF Converter

A simple **Django + Celery + Redis** application that converts uploaded images into a single PDF asynchronously.

This project is great for learning:

- Background job processing with Celery
- Redis as a broker/result backend
- File uploads in Django
- Async task monitoring
- Clean separation between web and worker layers

---

## 🚀 Features

✅ Upload one or multiple images  
✅ Convert images into a PDF in the background  
✅ Non‑blocking UI  
✅ Download generated file  
✅ Scalable worker architecture  

---

## 🧠 Architecture Overview

User → Django Web App → Redis Queue → Celery Worker → PDF Generated → User Download

---

## 📦 Tech Stack

- Python  
- Django  
- Celery  
- Redis  
- FPDF / Pillow (depending on implementation)

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mathurdanduprolu/img2pdf.git
cd img2pdf
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
# .venv\Scripts\activate  # windows
```

### 3. Install dependencies

If you have requirements.txt:

```bash
pip install -r requirements.txt
```

Otherwise install common ones:

```bash
pip install django celery redis fpdf pillow
```

---

## 🟥 Start Redis

### Option A – Local install
mac:
```bash
brew install redis
brew services start redis
```

linux:
```bash
sudo systemctl start redis
```

### Option B – Docker
```bash
docker run --name redis -p 6379:6379 -d redis:7
```

---

## ▶️ Run Django

```bash
cd image_to_pdf_project
python manage.py migrate
python manage.py runserver
```

App will be available at:

```
http://127.0.0.1:8000/
```

---

## ⚡ Start Celery Worker (new terminal)

```bash
cd image_to_pdf_project
celery -A image_to_pdf_project worker -l info
```

---

## 🧪 How It Works

1. User uploads images.
2. Django sends a task to Redis.
3. Celery worker picks the task.
4. Worker merges images → creates PDF.
5. Result becomes available for download.

---

## 🛠 Common Errors & Fixes

**Redis connection refused**  
→ Ensure Redis is running on port 6379.

**Celery cannot find module**  
→ Run command from folder containing `manage.py`.

**Static files missing**  
```bash
python manage.py collectstatic
```

---

## 🌟 Why this project is useful

If you want to become:

- Applied AI / Enterprise AI Engineer  
- Backend or Platform Engineer  
- Staff+ level system designer  

understanding async pipelines like this is foundational.

---

## 👤 Author

**Mathur Danduprolu**  
SAP → AI/Backend transition journey 🚀

If this helped you, consider giving the repo a ⭐

---
