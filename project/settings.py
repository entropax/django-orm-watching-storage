import os
from environs import Env
import dj_database_url

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG")

DATABASES = {"default": env.dj_db_url("DB_URL")}

INSTALLED_APPS = ["datacenter"]

SECRET_KEY = env("SECRET_KEY")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ["localhost", "0.0.0.0"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]

USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True
