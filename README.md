# 🌍 alxtravelapp

A scalable Django-based travel listing platform that allows users to browse listings, make bookings, and leave reviews. Designed with modularity, team collaboration, and industry best practices in mind.

---

## 🚀 Project Overview

`alxtravelapp` is a backend API built with Django and Django REST Framework to power a travel platform. It features listing management, bookings, and review capabilities. The app is configured to use MySQL as the primary database and includes Swagger for automated API documentation.

---

## 📚 Features

- Modular Django project structure
- Listings with details, price, and availability
- Booking system for users
- Review system with rating and comment
- RESTful API with DRF
- Swagger API documentation via `drf-yasg`
- Environment variable management via `django-environ`
- CORS support for frontend-backend communication
- Celery and RabbitMQ setup for future background tasks
- Faker-powered seed script for generating sample data

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **API Docs:** Swagger (drf-yasg)
- **Async Tasks:** Celery, RabbitMQ
- **Environment Management:** django-environ
- **Version Control:** Git

---

## 🧱 Project Structure

```bash
alxtravelapp/
├── alxtravelapp/            # Project settings and URLs
├── listings/                # Core app for Listings, Bookings, Reviews
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── seed.py      # Seeder script
├── requirements.txt         # Dependencies
├── .env                     # Environment variables (not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/alxtravelapp.git
cd alxtravelapp
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` File

Create a `.env` file in the root directory and include:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed the Database

Generate fake listings for development:

```bash
python manage.py seed
```

### 7. Run the Server

```bash
python manage.py runserver
```

---

## 📘 API Documentation

After starting the server, visit:

```
http://localhost:8000/swagger/
```

> Automatically generated with `drf-yasg` Swagger UI.

---

## 🔁 Running the Worker (For Celery Tasks)

*Assuming RabbitMQ is installed and running:*

```bash
celery -A alxtravelapp worker -l info
```

---

## ✅ Testing

To run Django tests:

```bash
python manage.py test
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Push to your fork (`git push origin feature/my-feature`)
5. Create a Pull Request

---

## 📦 Dependencies

- Django
- djangorestframework
- django-cors-headers
- drf-yasg
- django-environ
- mysqlclient
- celery
- faker
