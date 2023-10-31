from django.urls import path
from safe_secret.apps import SafeSecretConfig
from safe_secret.views import SecretCreateAPIView, SecretRetrieveAPIView

app_name = SafeSecretConfig.name


urlpatterns = [
    path('secret/', SecretCreateAPIView.as_view(), name='secret_create'),
    path('secret/<str:code_phrase>/', SecretRetrieveAPIView.as_view(), name='secret_show'),
]
