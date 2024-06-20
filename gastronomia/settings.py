"""
Django settings for gastronomia project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-etbh1t4-!_wtkk!so=jyx7$g7u5+4s)7wg$=lj$1jpl@l6*&b2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Não mostrará mensagens de erro com ele em False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.aluno03.cursopython.dev.br',
                 'aluno03.cursopython.dev.br']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apis',

    'rest_framework',
    'django_filters',
    'rest_framework.authtoken'  # Aqui se diz que usará a utilização por token
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gastronomia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gastronomia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cursopython_dbescola03',
        'HOST': 'cursopython.dev.br',
        'PORT': '3306',
        'USER': 'cursopython_adm03',
        'PASSWORD': 'Curso+2024',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
# Configura o método de autenticação (verificação de quem está usando)
# e permissão (o que a pessoa pode fazer/se autenticado, faz tudo
# caso contrário, ela pode apenas ler) da api


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # Aqui, estou me autenticando por usuário/senha pela sessão - exige tela de login.
        # O padrão hoje em dia é utilizar o conceito de token - chave é dada para o usuário
        # A chave é usada quando for chamar a api
        'rest_framework.authentication.TokenAuthentication',
        # Para autenticar por token, o Django Rest Framework tem uma aplicação própria
        # Deve ser executado o python manage.py migrate após isso
        # Token deve ser gerado no admin
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # Não tendo outra classe, essa vale / autenticado faz tudo, não autenticado só lê
        # Se não colocar controle na view, vale essa
    ]
}

# Como o projeto Django vai se comportar. No primeiro, como se comportará na autenticação e,
# no segundo, como
