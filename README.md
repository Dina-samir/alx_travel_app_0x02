
# 🧳 ALX Travel App

A travel listings application built with Django and Django REST Framework (DRF). It allows users to manage and retrieve travel-related listings via RESTful APIs.

## 📁 Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/     # Django project settings
├── listings/                # Custom app for travel listings
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Features

- Travel listings management (`listings` app)
- RESTful API with Django REST Framework
- CORS enabled for frontend integration
- API Documentation with Swagger (drf_yasg)

## 🛠️ Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger/OpenAPI)
- CORS Headers

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Dina-samir/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv env
source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create the `listings` app (if not already created)**

```bash
python manage.py startapp listings
```

5. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the development server**

```bash
python manage.py runserver
```

## 🔌 API Documentation

Visit: [http://localhost:8000/swagger/](http://localhost:8000/swagger/) to explore the API using Swagger UI (powered by `drf-yasg`).

## 🛡️ Installed Apps (`settings.py`)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'drf_yasg',

    'listings',  # Custom app
]
```

## 📦 Example `requirements.txt`

```
Django>=4.0
djangorestframework
drf-yasg
django-cors-headers
```

## ✨ Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request


