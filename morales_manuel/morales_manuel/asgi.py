"""
<<<<<<< HEAD
ASGI config for morales_manuel project.
=======
ASGI config for mi_proyecto project.
>>>>>>> fa8fbcd3d6beed70299ec3a08cf0d1eb070685ee

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morales_manuel.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
>>>>>>> fa8fbcd3d6beed70299ec3a08cf0d1eb070685ee

application = get_asgi_application()
