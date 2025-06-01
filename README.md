# InstaLoad

> **InstaLoad** — міні-сервіс для швидкого завантаження відео, фото, Reels та Story з Instagram у два кліки. Побудований на Django 5 та Bootstrap 5. Легко розгортається на Render.com без окремого web-сервера — статичні файли обслуговує Whitenoise.

---

## 📸 Основні можливості

| Функція | Опис |
|---------|-------|
| **Video Downloader** | Завантаження одного чи декількох відео з каруселей. |
| **Photo Downloader** | Збереження окремих фото або цілих каруселей. |
| **Reels Downloader** | Отримання будь-яких Reels за посиланням. |
| **Story Downloader** | Збереження Story навіть після 24 годин. |
| **FAQ-секція**       | Тримай курсор на «FAQ» у навігації — швидкі відповіді. |

---

## 🖼️ Інтерфейс

<div align="center">
  <img src="docs/screenshot_home.png" width="700" alt="Головна сторінка">
</div>

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
