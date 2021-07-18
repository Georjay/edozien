# edozien

[![Python Version](https://img.shields.io/badge/python-3.9.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.1-brightgreen.svg)](https://djangoproject.com)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-v.4-brightgreen.svg)](https://getbootstrap.com/)

This is a personal website for Chike Frankie Edozien. It gives it's user the ability to write blogs and archive events.

## Screenshots
![edozien](https://raw.githubusercontent.com/Georjay/screenshots/main/edozien.png)

## Running the Project Locally

First, clone the repository to your local machine:

CMD:

```bash
git clone https://github.com/Georjay/edozien.git
```

GitHub CLI:

```bash
gh repo clone Georjay/edozien
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## Extras

Note that variables have been used in the settings.py
