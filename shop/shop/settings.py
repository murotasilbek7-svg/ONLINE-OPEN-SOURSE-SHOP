

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'U2FsdGVkX19HfyFOoxXRDqTWchsSSoA+FiX94u0ViVHDkf8pIlGJRHW09Bq7ACb7pmxplFcnDZRU4VQgKkIGIJxinOprCuxzsBqo4h2oR1SHLCfK5HWpii9dT3aqZ/jxSbQ8ApCg6uYsEEwe9DQRDLrFLecLRia7pGd4mcpruD/9W6QAYXsDXVOzyEpFiUU6juPoWFjd1zSrc4Q+DcmbqDog2t5ldAm9VqJVxSmdhcfdSWd+vcZuV1mfMtlWKztoDaPcDqcX8jBmfDLlLYDGiRrCqJgWj/pic4IZgEVfkfuNnkhtWdpBVN0cH5OYt8KOA0eeUYXqDGjtIUf9V+m6T2IkqKJVg7TxeWxKxtKrOXyMbCX74WGpu0DmpRHscEF3EsOVnVGndJifCI89B81BXlgAgQ1279TnJHkOTkU6ypUnvb30hmu3Q8B3EECkrkhDGL7tibwOhdhC1mY+frjexHorsdTWaTc3jc/bSfzQL0KOowgdrisMCGA5tUjlpoiTq3SmB/rnywkmoVoxjp6b7Z7xhBIntsaNf5fujx8mf/TqukfrjT9FrQrmkiypXZoe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
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

ROOT_URLCONF = 'shop.urls'

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

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
