#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="image_to_pdf_project"

cat <<'TXT'
============================================================
img2pdf — Image to PDF Converter (Django + Celery + Redis)
============================================================

This project is a Django web app that lets users upload images and converts them into a PDF
asynchronously using Celery with Redis as the broker/backing service.

What you get:
- Upload images from the UI
- Conversion happens in the background (Celery worker)
- Download the generated PDF when ready

------------------------------------------------------------
Quick Start (local)
------------------------------------------------------------

1) Prerequisites
- Python 3.x
- Redis (local install or Docker)
- (Optional) Node/npm only if you rebuild Tailwind locally

2) Create a virtualenv + install deps (example)
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip

If you have a requirements.txt, install it:
    pip install -r requirements.txt

If you DON'T have requirements.txt, install typical deps:
    pip install django celery redis fpdf

3) Start Redis
- macOS (Homebrew):   brew install redis && brew services start redis
- Linux (systemd):    sudo systemctl start redis
- Docker:
    docker run --name redis -p 6379:6379 -d redis:7

4) Run Django migrations + start server
    cd image_to_pdf_project
    python manage.py migrate
    python manage.py runserver

5) Start Celery worker (new terminal, same venv)
    cd image_to_pdf_project
    celery -A image_to_pdf_project worker -l info

Open:
    http://127.0.0.1:8000/

------------------------------------------------------------
Common Troubleshooting
------------------------------------------------------------

- "Connection refused" to Redis:
  Make sure Redis is running on localhost:6379 (or update CELERY_BROKER_URL)

- Celery can't find the app:
  Run the worker from the same folder where manage.py lives and ensure the -A module matches your project.

- Static/Tailwind not loading:
  If you use Django staticfiles, run:
      python manage.py collectstatic
  (Tailwind build steps depend on how you wired it.)

------------------------------------------------------------
Where to find more details
------------------------------------------------------------
This repo is tied to a Medium tutorial referenced in the README.
TXT

echo
echo "Repo layout (expected):"
echo "  - ${PROJECT_DIR}/   (Django project root, contains manage.py)"
echo "  - input/            (optional sample inputs)"
echo

# Optional interactive mode
if [[ "${1:-}" == "--run" ]]; then
  echo ">>> Running a guided setup (best effort)."
  echo ">>> NOTE: This will not install Redis for you."

  if [[ ! -d ".venv" ]]; then
    python3 -m venv .venv
  fi
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install --upgrade pip

  if [[ -f "requirements.txt" ]]; then
    pip install -r requirements.txt
  else
    pip install django celery redis fpdf
  fi

  if [[ -d "${PROJECT_DIR}" ]]; then
    cd "${PROJECT_DIR}"
    python manage.py migrate
    echo ">>> Starting Django server at http://127.0.0.1:8000/"
    python manage.py runserver
  else
    echo "ERROR: Can't find ${PROJECT_DIR}/"
    exit 1
  fi
fi

echo
echo "Tip: chmod +x README.sh && ./README.sh"
echo "     or: ./README.sh --run   (attempts local setup + starts server)"
