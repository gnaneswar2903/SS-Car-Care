"""
Django settings for config project.
"""

from pathlib import Path


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = 'django-insecure-da5=n+&6ftr-@(4!-fyyb@h(o)9f6+q%1t1r9v&gj2zwn*ylia'

DEBUG = True

ALLOWED_HOSTS = []


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Jazzmin
    'jazzmin',

    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'home',
]


# ============================================================
# JAZZMIN SETTINGS
# ============================================================

JAZZMIN_SETTINGS = {

    "site_title": "SS Car Care Admin",
    "site_header": "SS Car Care",
    "site_brand": "SS Car Care",

    "welcome_sign": "Welcome to SS Car Care Administration",
    "copyright": "SS Car Care",

    "site_logo": None,
    "login_logo": None,

    "search_model": [
        "auth.User",
        "auth.Group",
    ],

    "topmenu_links": [
        {
            "name": "Website",
            "url": "home",
            "permissions": ["auth.view_user"],
        },
    ],

    "usermenu_links": [],

    "show_sidebar": True,
    "navigation_expanded": True,

    "hide_apps": [],
    "hide_models": [],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,

    "custom_css": None,
    "custom_js": None,

    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",

    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },

    "language_chooser": False,
}


# ============================================================
# JAZZMIN UI TWEAKS
# ============================================================

JAZZMIN_UI_TWEAKS = {

    "theme": "default",
    "dark_mode_theme": "darkly",

    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,

    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,

    "actions_sticky_top": True,

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = 'config.urls'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = 'config.wsgi.application'


# ============================================================
# DATABASE
# ============================================================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# EMAIL
# ============================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'