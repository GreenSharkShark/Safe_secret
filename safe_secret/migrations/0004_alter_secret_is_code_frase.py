# Generated by Django 4.2.6 on 2023-10-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_secret', '0003_alter_secret_code_frase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='is_code_frase',
            field=models.BooleanField(default=False),
        ),
    ]