# Generated by Django 4.2.6 on 2023-10-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe_secret', '0005_alter_secret_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='code_frase',
            new_name='code_phrase',
        ),
        migrations.RenameField(
            model_name='secret',
            old_name='is_code_frase',
            new_name='is_code_phrase',
        ),
    ]
