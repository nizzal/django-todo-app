# Django Todo App

---

Simple Django Todo App

## Functionality

-   Add todo tasks
-   Edit todo Tasks

## Installation

```
git clone https://github.com/nizzal/django-todo-app
cd /django-todo-app
pip install -r requirements.txt
python manage.py runserver
```

## Build with Docker

```
git clone https://github.com/nizzal/django-todo-app
cd /django-todo-app
docker build -t django-todo-app .
docker run -it -p 8000:8000 django-todo-app
```
