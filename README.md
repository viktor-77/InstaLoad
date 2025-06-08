# InstaLoad

> **InstaLoad** — A mini-service for quickly downloading videos, photos, Reels and Stories from Instagram in two clicks. Built on Django 5 and Bootstrap 5. Easily deployed on Render.com without a separate web server — static files are served by Whitenoise.

---

## Main features

| Функція | Опис |
|---------|-------|
| **Video Downloader** | Download one or more videos from carousels. |
| **Photo Downloader** | Save individual photos or entire carousels. |
| **Reels Downloader** | Get any Reels via the link. |
| **Story Downloader** | Saving Story even after 24 hours. |
| **FAQ-секція**       | Hover over "FAQ" in the navigation for quick answers.|

---

## Інтерфейс

![img.png](img.png)

---

## 🔧 Технології

- **Python 3.11**, **Django 5.2**
- **Gunicorn** — WSGI-сервер
- **Whitenoise** — обслуговування статики
- **Bootstrap 5** & **Bootstrap Icons**
- **Requests** — звернення до RapidAPI-ендпоінтів Instagram

---

## 🚀 Запуск локально

```bash
git clone https://github.com/viktor-77/InstaLoad.git
cd InstaLoad
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Перейти на http://127.0.0.1:8000/


🚀 Запуск render.com

https://instaload-sl70.onrender.com/
