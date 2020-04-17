from apple.views import index, send_email
from django.urls import include, path


urlpatterns = [
    path('', index, name='index'),
    path('send-email/', send_email, name='send-email'),
]
