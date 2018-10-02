import os

from django.conf import settings
from izi import IZI_MAIN_TEMPLATE_DIR, get_core_apps
from izi.defaults import IZI_SETTINGS


def pytest_configure():
    location = lambda x: os.path.join(
        os.path.dirname(os.path.realpath(__file__)), x)

    test_settings = IZI_SETTINGS.copy()
    test_settings.update(dict(
        DATABASES={
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'izi_stores',
            }
        },
        SITE_ID=1,
        MEDIA_ROOT=location('public/media'),
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        STATICFILES_DIRS=(location('static/'),),
        STATIC_ROOT=location('public'),
        STATICFILES_FINDERS=(
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        ),
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    location('templates'),
                    IZI_MAIN_TEMPLATE_DIR,
                ],
                'OPTIONS': {
                    'loaders': [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ],
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.request',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.contrib.messages.context_processors.messages',
                    ],
                }
            }
        ],
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'izi.apps.basket.middleware.BasketMiddleware',
        ),
        ROOT_URLCONF='sandbox.sandbox.urls',
        TEMPLATE_DIRS=(
            location('templates'),
            IZI_MAIN_TEMPLATE_DIR,
        ),
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.admin',
            'django.contrib.gis',
            'django.contrib.flatpages',
            'widget_tweaks',
        ] + get_core_apps() + [
            'stores',
        ],
        AUTHENTICATION_BACKENDS=(
            'izi.apps.customer.auth_backends.EmailBackend',
            'django.contrib.auth.backends.ModelBackend',
        ),
        LOGIN_REDIRECT_URL='/accounts/',
        APPEND_SLASH=True,
        HAYSTACK_CONNECTIONS={
            'default': {
                'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
            },
        },
        GEOIP_PATH='sandbox/geoip',
        COMPRESS_ENABLED=False,
        TEST_RUNNER='django.test.runner.DiscoverRunner',
    ))

    settings.configure(**test_settings)
