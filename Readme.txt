     !!!! Muhim !!!!

rest_framework o'rnaish:
============================
pip install rest_framework
============================

CORS o‘rnatish
===============================
pip install django-cors-headers
===============================




CORS ulash
settings.py:
-----------------------------
INSTALLED_APPS = [
    ...
    'corsheaders',
]
-----------------------------

-------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
--------------------------------------------

--------------------------------------
CORS_ALLOW_ALL_ORIGINS = True
--------------------------------------




