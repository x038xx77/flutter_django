"""
ASGI config for web_med_plist project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# import src.videoch_chat
# from videoch_chat import routing
# from src.videoch_chat import routing
import chat.routing

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'web_med_plist.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # routing.websocket_urlpatterns
            chat.routing.websocket_urlpatterns
        )
    ),
})
