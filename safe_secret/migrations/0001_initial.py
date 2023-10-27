# Generated by Django 4.2.6 on 2023-10-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64, verbose_name='хэш')),
                ('ciphertext', models.TextField(verbose_name='зашифрованный текст')),
                ('link', models.CharField(max_length=250, verbose_name='ссылка')),
                ('lifetime', models.PositiveSmallIntegerField(verbose_name='время жизни')),
                ('code_frase', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'секрет',
                'verbose_name_plural': 'секреты',
            },
        ),
    ]