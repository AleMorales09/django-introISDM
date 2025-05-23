"""
<<<<<<< HEAD
WSGI config for morales_manuel project.
=======
WSGI config for mi_proyecto project.
>>>>>>> fa8fbcd3d6beed70299ec3a08cf0d1eb070685ee

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morales_manuel.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
>>>>>>> fa8fbcd3d6beed70299ec3a08cf0d1eb070685ee

application = get_wsgi_application()
