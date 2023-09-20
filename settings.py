import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'yourappname.apps.YourAppNameConfig',  # Add your app here
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Use the default authentication backend
]

LOGIN_URL = 'login'  # URL where users will be redirected for login
LOGOUT_URL = 'logout'  # URL to handle user logout
LOGIN_REDIRECT_URL = 'dashboard'  # URL to redirect to after successful login
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
