# Generated by Django 4.2.6 on 2023-10-30 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe_secret', '0008_alter_secret_time_to_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='ciphertext',
            new_name='secret_text',
        ),
    ]
