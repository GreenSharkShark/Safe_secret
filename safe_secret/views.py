import secrets
from rest_framework import generics, status
from rest_framework.response import Response
from safe_secret.models import Secret
from safe_secret.serializers import SecretSerializer, SecretRetrieveSerializer
from safe_secret.services import sha256_hash, Encryptor, make_link
from django.utils import timezone


class SecretCreateAPIView(generics.CreateAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    def perform_create(self, serializer):
        secret = serializer.save()

        text = serializer.validated_data.get('secret_text')
        secret.secret_text = Encryptor().encrypt_text(text)

        code_phrase = serializer.validated_data.get('code_phrase')
        if code_phrase:
            secret.code_phrase = sha256_hash(code_phrase)
            secret.is_code_phrase = True
        # генерируется случайная строка вместо хэша, если кодовая фраза не была задана
        else:
            secret.code_phrase = secrets.token_hex(32)

        link = make_link(secret.code_phrase)
        secret.link = link

        secret.time_to_delete = timezone.now() + timezone.timedelta(minutes=secret.lifetime)

        secret.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        link = response.data.get('link')
        return Response({'link': link}, status=status.HTTP_201_CREATED)


class SecretRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SecretRetrieveSerializer
    queryset = Secret.objects.all()

    def retrieve(self, request, *args, **kwargs):
        code_phrase = self.kwargs.get('code_phrase')
        try:
            secret = Secret.objects.get(code_phrase=code_phrase)
        except Secret.DoesNotExist:
            return Response({'error': 'Такого объекта не существует. Вы воспользовались неверной ссылкой, '
                                      'либо данные по ссылке уже были просмотрены и удалены.'},
                            status=status.HTTP_404_NOT_FOUND)

        if secret.is_code_phrase is True:
            code_phrase = request.data.get('code_phrase')
            hashed_phrase = sha256_hash(code_phrase)
            if hashed_phrase != secret.code_phrase:
                return Response({'error': 'Неверная кодовая фраза'}, status=status.HTTP_400_BAD_REQUEST)

        plaintext = Encryptor().decrypt_text(secret.secret_text)
        serializer = self.get_serializer(data={'secret_text': plaintext})
        serializer.is_valid(raise_exception=True)

        secret.delete()

        return Response(serializer.data)


class SecrestDestroyAPIView(generics.DestroyAPIView):
    queryset = Secret.objects.all()
    lookup_field = 'code_phrase'
