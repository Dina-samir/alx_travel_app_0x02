
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


## 🗂️ Models

### Listing
| Field            | Type         | Description                  |
|------------------|--------------|------------------------------|
| id               | UUID         | Primary key                  |
| title            | string       | Listing title                |
| description      | text         | Description of the listing   |
| price_per_night  | decimal      | Price per night              |
| location         | string       | Location of the listing      |
| host             | User (FK)    | Host user                    |
| created_at       | datetime     | Creation timestamp           |

### Booking
| Field        | Type         | Description                        |
|--------------|--------------|------------------------------------|
| id           | UUID         | Primary key                        |
| listing      | Listing (FK) | The listing being booked           |
| guest        | User (FK)    | The guest making the booking       |
| start_date   | date         | Booking start date                 |
| end_date     | date         | Booking end date                   |
| status       | string       | Booking status (pending/confirmed/cancelled) |
| created_at   | datetime     | Creation timestamp                 |

### Review
| Field        | Type         | Description                        |
|--------------|--------------|------------------------------------|
| id           | UUID         | Primary key                        |
| listing      | Listing (FK) | The listing being reviewed         |
| user         | User (FK)    | The user leaving the review        |
| rating       | integer      | Rating (1-5)                       |
| comment      | text         | Review comment                     |
| created_at   | datetime     | Creation timestamp                 |

## 📬 API Usage Examples

### List all listings
**GET** `/api/listings/`

### Retrieve a single listing
**GET** `/api/listings/{id}/`

### Create a new listing
**POST** `/api/listings/`
```json
{
  "host": 1,
  "title": "Cozy Home",
  "description": "A beautiful home perfect for vacations.",
  "location": "City",
  "price_per_night": "120.00"
}
```

### List all bookings
**GET** `/api/bookings/`

### Create a new booking
**POST** `/api/bookings/`
```json
{
  "listing": "<listing_uuid>",
  "guest": 2,
  "start_date": "2025-08-10",
  "end_date": "2025-08-12",
  "status": "pending"
}
```

### List all reviews (if endpoint added)
**GET** `/api/reviews/`

## ✨ Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request


